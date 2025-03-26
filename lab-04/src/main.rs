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
        n => {
            let mut det = 0.0;

            for j in 0..n {
                let minor = get_minor(matrix, 0, j);
                det += (-1.0_f64).powf(j as f64) * matrix[0][j] * self::det(&minor);
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

fn main() {
    let square_matrix = vec![
        vec![2.0, 4.0],
        vec![1.0, 3.0]
    ];

    let det = det(&square_matrix);
    println!("{}", det);

    let big_square_matrix = vec![
        vec![2.0, 4.0, 3.0],
        vec![1.0, 3.0, 2.0],
        vec![1.0, 2.0, 3.0]
    ];

    let det = crate::det(&big_square_matrix);
    println!("{}", det);

    let matrix = vec![
        vec![1.0, 2.0, 3.0],
        vec![4.0, 5.0, 6.0]
    ];

    let transposed = transpose(&matrix);
    print(&transposed);

    let inverse = invert_laplacian(&big_square_matrix).unwrap();
    print(&inverse);

    let inverse = invert_gauss_jordan(&big_square_matrix).unwrap();
    print(&inverse);
}
