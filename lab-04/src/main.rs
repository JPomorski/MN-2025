type Matrix = Vec<Vec<f64>>;

fn is_matrix_square(matrix: &Matrix) -> bool {
    let row_count = matrix.len();

    for row in matrix {
        if row.len() != row_count {
            return false;
        }
    }

    true
}

fn get_square_matrix_size(matrix: &Matrix) -> usize {
    matrix.len()
}

fn get_matrix_size(matrix: &Matrix) -> (usize, usize) {
    (matrix.len(), matrix[0].len())
}

fn get_minor(matrix: &Matrix, i: usize, j: usize) -> Matrix {
    let mut minor = matrix.clone();
    minor.remove(i);

    for mut row in &mut minor {
        row.remove(j);
    }

    minor
}

fn det(matrix: &Matrix) -> f64 {
    match get_square_matrix_size(matrix) {
        1 => matrix[0][0],
        2 => (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]),
        3 => {
            let n = get_square_matrix_size(matrix);
            let mut sarrus_matrix = vec![vec![0.0; n + 2]; n];

            for i in 0..n {
                for j in 0..n {
                    sarrus_matrix[i][j] = matrix[i][j];
                }
            }

            for i in 0..n {
                for j in 0..2 {
                    sarrus_matrix[i][n + j] = matrix[i][j];
                }
            }

            let mut det = 0.0;
            let mut offset = 0;

            for _ in 0..3 {
                let mut d = 1.0;

                for j in 0..n {
                    // println!("{}:{}", j, j + offset);
                    d *= sarrus_matrix[j][j + offset];
                }

                // println!("d = {}", d);

                det += d;
                offset += 1;
            }

            let mut offset = 0;

            for _ in 0..3 {
                let mut d = 1.0;

                for j in (0..n).rev() {
                    // println!("{}:{}", (n - 1) - j, j + offset);
                    d *= sarrus_matrix[(n - 1) - j][j + offset];
                }

                // println!("d = {}", d);

                det -= d;
                offset += 1;
            }

            det
        }
        n => {
            let mut det = 0.0;

            for j in 0..n {
                let c = get_minor(matrix, 0, j);
                det += (-1.0_f64).powf(j as f64) * matrix[0][j] * self::det(&c);
            }

            det
        }
    }
}

fn transpose(matrix: &Matrix) -> Matrix {
    let (m, n) = get_matrix_size(matrix);
    let mut transposed = vec![vec![0.0; m]; n];

    for i in 0..m {
        for j in 0..n {
            transposed[j][i] = matrix[i][j];
        }
    }

    transposed
}

fn multiply(matrix1: &Matrix, matrix2: &Matrix) -> Matrix {
    let rows_a = matrix1.len();
    let cols_a = matrix1[0].len();
    let cols_b = matrix2[0].len();

    let mut result: Vec<Vec<f64>> = vec![vec![0.0; cols_b]; rows_a];

    for row_a in 0..rows_a {
        for col_b in 0..cols_b {
            for col_a in 0..cols_a {
                result[row_a][col_b] += matrix1[row_a][col_a] * matrix2[col_a][col_b];
            }
        }
    }

    result
}

fn get_cofactor(matrix: &Matrix) -> Matrix {
    let n = get_square_matrix_size(matrix);
    let mut cofactor = vec![vec![0.0; n]; n];

    for i in 0..n {
        for j in 0..n {
            let minor = get_minor(matrix, i, j);
            let minor_det = det(&minor);
            cofactor[i][j] = (-1.0_f64).powf((i + j) as f64) * minor_det
        }
    }

    cofactor
}

fn invert_laplacian(matrix: &Matrix) -> Option<Matrix> {
    let det = det(matrix);

    if det == 0.0 {
        println!("Nie można odwrócić macierzy o wyznaczniku 0!");
        return None;
    }

    let cofactor = get_cofactor(matrix);
    let mut adj = transpose(&cofactor);

    let n = get_square_matrix_size(&adj);

    for i in 0..n {
        for j in 0..n {
            adj[i][j] /= det;
        }
    }

    Some(adj)
}

fn invert_gauss_jordan(matrix: &Matrix) -> Option<Matrix> {
    let det = det(matrix);

    if det == 0.0 {
        println!("Nie można odwrócić macierzy o wyznaczniku 0!");
        return None;
    }

    let n = get_square_matrix_size(matrix);
    let mut augmented = vec![vec![0.0; n * 2]; n];

    for i in 0..n {
        for j in 0..n {
            augmented[i][j] = matrix[i][j];
        }
        augmented[i][n + i] = 1.0
    }

    for i in 0..n {
        let mut max_row = i;
        let mut max_val = augmented[i][i].abs();

        for j in (i + 1)..n {
            if augmented[j][i].abs() > max_val {
                max_val = augmented[j][i].abs();
                max_row = j;
            }
        }

        if max_row != i {
            augmented.swap(i, max_row);
        }

        let pivot = augmented[i][i];
        for j in 0..(2 * n) {
            augmented[i][j] /= pivot;
        }

        for j in 0..n {
            if j != i {
                let factor = augmented[j][i];
                for k in 0..(2 * n) {
                    augmented[j][k] -= factor * augmented[i][k];
                }
            }
        }
    }

    let mut inverse = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            inverse[i][j] = augmented[i][n + j]
        }
    }

    Some(inverse)
}

fn print(matrix: &Matrix) {
    for row in matrix {
        println!("{:?}", row);
    }
}

fn print_round(matrix: &Matrix) {
    for row in matrix {
        println!("{:?}", row.iter().map(|x| x.round().abs()).collect::<Vec<f64>>());
    }
}

fn main() {
    println!("Zadanie 1:");

    let square_matrix = vec![
        vec![2.0, 4.0],
        vec![1.0, 3.0]
    ];

    print(&square_matrix);

    let det = det(&square_matrix);
    println!("{}", det);

    let big_square_matrix = vec![
        vec![2.0, 4.0, 3.0],
        vec![1.0, 3.0, 2.0],
        vec![1.0, 2.0, 3.0]
    ];

    print(&big_square_matrix);

    let det = crate::det(&big_square_matrix);
    println!("{}", det);

    let przyklad = vec![
        vec![15.0, 11.0, 10.0, 15.0],
        vec![19.0, 9.0, 0.0, 17.0],
        vec![6.0, 9.0, 6.0, 13.0],
        vec![0.0, 12.0, 12.0, 11.0]
    ];

    print(&przyklad);

    let det = crate::det(&przyklad);
    println!("{}", det);

    println!();

    println!("Zadanie 2:");

    let transposed = transpose(&square_matrix);
    print(&transposed);

    println!();

    let matrix = vec![
        vec![1.0, 2.0, 3.0],
        vec![4.0, 5.0, 6.0]
    ];

    let transposed = transpose(&matrix);
    print(&transposed);

    println!();

    println!("Zadanie 3:");

    let inv = invert_gauss_jordan(&przyklad).unwrap();
    print(&inv);

    let det = crate::det(&inv);
    println!("{}", det);

    println!();

    let aaa = multiply(&przyklad, &inv);
    print(&aaa);

    println!();

    let aaa = multiply(&inv, &przyklad);
    print(&aaa);

    println!();

    let inverse = invert_laplacian(&big_square_matrix).unwrap();
    print(&inverse);

    println!();

    let inverse = invert_gauss_jordan(&big_square_matrix).unwrap();
    print(&inverse);

    println!("==================");

    let inverse = invert_laplacian(&przyklad).unwrap();
    print(&inverse);

    println!();

    let inverse = invert_gauss_jordan(&przyklad).unwrap();
    print(&inverse);
}
