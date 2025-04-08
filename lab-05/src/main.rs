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
        println!("{:>5.1?}", row);
    }
}

fn print_round(matrix: &Matrix) {
    for row in matrix {
        println!("{:>5.1?}", row.iter().map(|x| x.round().abs()).collect::<Vec<f64>>());
    }
}

fn doolittle(matrix: &Matrix) -> (Matrix, Matrix) {
    let n = get_square_matrix_size(&matrix);

    let mut vec_u = vec![vec![0.0; n]; n];
    let mut vec_l = vec![vec![0.0; n]; n];

    for i in 0..3 {
        vec_l[i][i] = 1.0
    }

    for i in 0..n {
        for j in i..n {
            let mut sum_u = 0.0;
            let mut sum_l = 0.0;

            for k in 0..i {
                sum_u += vec_l[i][k] * vec_u[k][j];
                sum_l += vec_l[j][k] * vec_u[k][i];
            }

            vec_u[i][j] = matrix[i][j] - sum_u;
            vec_l[j][i] = (matrix[j][i] - sum_l) / vec_u[i][i];
        }
    }

    (vec_l, vec_u)
}

fn solve_linear_equation(l_matrix: &Matrix, u_matrix: &Matrix, b: &Matrix) -> Matrix {
    let n = get_square_matrix_size(l_matrix);
    let mut y = vec![vec![0.0]; n];

    for i in 0..n {
        let mut sum = 0.0;

        for j in 0..i {
            sum += l_matrix[i][j] * y[j][0]
        }

        y[i][0] = sum * -1.0 + b[i][0]
    }

    let mut x = vec![vec![0.0]; n];

    for i in (0..n).rev() {
        let mut sum = 0.0;

        for j in ((i + 1)..n).rev() {
            sum += u_matrix[i][j] * x[j][0]
        }

        x[i][0] = (sum * -1.0 + y[i][0]) / u_matrix[i][i];
    }

    x
}

fn measure_zad_01(a: &Matrix, b: &Matrix) {
    let start = std::time::Instant::now();

    let inv_lap = invert_laplacian(&a).unwrap();
    let result = multiply(&inv_lap, &b);

    let elapsed = start.elapsed().as_secs_f64();

    println!("Macierz wejściowa:");
    print(&a);
    println!(" ");

    println!("Macierz odwrotna:");
    print(&inv_lap);
    println!(" ");

    println!("Wynik:");
    print(&result);
    println!(" ");

    println!("Elapsed (Laplace): {}", elapsed);
    println!(" ");

    let start = std::time::Instant::now();

    let inv_gauss = invert_gauss_jordan(&a).unwrap();
    let result = multiply(&inv_gauss, &b);

    let elapsed = start.elapsed().as_secs_f64();

    println!("Macierz wejściowa:");
    print(&a);
    println!(" ");

    println!("Macierz odwrotna:");
    print(&inv_gauss);
    println!(" ");

    println!("Wynik:");
    print(&result);
    println!(" ");

    println!("Elapsed (Gauss): {}", elapsed);
    println!(" ");
}

fn measure_zad_02(a: &Matrix, b: &Matrix) {
    let start = std::time::Instant::now();

    let (l, u) = doolittle(&a);
    let result = solve_linear_equation(&l, &u, &b);

    let elapsed = start.elapsed().as_secs_f64();

    let a = multiply(&l, &u);

    println!("Macierz L:");
    print(&l);
    println!(" ");

    println!("Macierz U:");
    print(&u);
    println!(" ");

    println!("Macierz L * U:");
    print(&a);
    println!(" ");

    println!("Macierz wejściowa:");
    print(&a);
    println!(" ");

    println!("Wynik:");
    print(&result);
    println!(" ");

    println!("Elapsed (LU): {}", elapsed);
    println!(" ");
}

fn main() {
    let a1 = vec![
        vec![1.0, 2.0, 1.0],
        vec![3.0, -7.0, 2.0],
        vec![2.0, 4.0, 5.0]
    ];

    let b1 = vec![
        vec![-9.0],
        vec![61.0],
        vec![-9.0]
    ];

    let a2 = vec![
        vec![11.0, -5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        vec![-5.0, 11.0, -5.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        vec![0.0, -5.0, 11.0, -5.0, 0.0, 0.0, 0.0, 0.0],
        vec![0.0, 0.0, -5.0, 11.0, -5.0, 0.0, 0.0, 0.0],
        vec![0.0, 0.0, 0.0, -5.0, 11.0, -5.0, 0.0, 0.0],
        vec![0.0, 0.0, 0.0, 0.0, -5.0, 11.0, -5.0, 0.0],
        vec![0.0, 0.0, 0.0, 0.0, 0.0, -5.0, 11.0, -5.0],
        vec![0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -5.0, 11.0]
    ];

    let b2 = vec![
        vec![11.0],
        vec![0.0],
        vec![0.0],
        vec![0.0],
        vec![0.0],
        vec![0.0],
        vec![0.0],
        vec![0.0],
    ];

    let a3 = vec![
        vec![1.0, 6.0, 3.0, 8.0, 7.0, 6.0, 9.0, 4.0, 7.0, 3.0],
        vec![0.0, 8.0, 8.0, 4.0, 6.0, 7.0, 5.0, 2.0, 2.0, 2.0],
        vec![3.0, 3.0, 7.0, 7.0, 1.0, 6.0, 9.0, 1.0, 2.0, 10.0],
        vec![6.0, 9.0, 6.0, 9.0, 5.0, 10.0, 6.0, 1.0, 8.0, 4.0],
        vec![2.0, 1.0, 9.0, 4.0, 6.0, 7.0, 8.0, 8.0, 7.0, 5.0],
        vec![10.0, 6.0, 2.0, 7.0, 7.0, 2.0, 10.0, 6.0, 10.0, 7.0],
        vec![7.0, 1.0, 8.0, 9.0, 1.0, 4.0, 10.0, 6.0, 5.0, 3.0],
        vec![7.0, 1.0, 9.0, 6.0, 9.0, 3.0, 8.0, 10.0, 9.0, 7.0],
        vec![9.0, 6.0, 8.0, 7.0, 7.0, 2.0, 3.0, 10.0, 5.0, 10.0],
        vec![10.0, 6.0, 6.0, 5.0, 9.0, 2.0, 0.0, 9.0, 2.0, 2.0],
    ];

    let b3 = vec![
        vec![5.0],
        vec![10.0],
        vec![10.0],
        vec![6.0],
        vec![4.0],
        vec![10.0],
        vec![9.0],
        vec![0.0],
        vec![7.0],
        vec![2.0],
    ];

    println!("Zadanie 1:");
    println!();

    measure_zad_01(&a1, &b1);
    measure_zad_01(&a2, &b2);
    measure_zad_01(&a3, &b3);

    println!("Zadanie 2:");
    println!();

    measure_zad_02(&a1, &b1);
    measure_zad_02(&a2, &b2);
    measure_zad_02(&a3, &b3);
}
