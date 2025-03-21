fn euclidean_norm(vec: &Vec<f64>) -> f64 {
    let square_sum = vec.iter().map(|x| x * x).sum::<f64>();
    square_sum.sqrt()
}

fn manhattan_norm(vec: &Vec<f64>) -> f64 {
    vec.iter().map(|x| x.abs()).sum::<f64>()
}

fn maximum_norm(vec: &Vec<f64>) -> f64 {
    vec.iter()
        .map(|&x| x.abs())
        .max_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap()
}

fn euclidean_metric(p: (f64, f64), q: (f64, f64)) -> f64 {
    let dx = p.0 - q.0;
    let dy = p.1 - q.1;
    (dx.powf(2.0) + dy.powf(2.0)).sqrt()
}

fn manhattan_metric(p: (f64, f64), q: (f64, f64)) -> f64 {
    let dx = (q.0 - p.0).abs();
    let dy = (q.1 - p.1).abs();
    dx + dy
}

fn metryka_rzeki(p: (f64, f64), q: (f64, f64)) -> f64 {
   p.1.abs() + (q.0 - p.0).abs() + q.1.abs()
}

fn metryka_kolejowa(p: (f64, f64), q: (f64, f64)) -> f64 {
    if (p.0 * q.1) - (p.1 * q.0) == 0.0 {
        euclidean_metric(p, q)
    } else {
        euclidean_metric(p, (0.0, 0.0)) + euclidean_metric(q, (0.0, 0.0))
    }
}

fn matrix_frobenius(matrix: &Vec<Vec<f64>>) -> f64 {
    let sum_a = matrix.iter()
        .map(|row| row.iter().map(|a| a.powf(2.0)).sum::<f64>())
        .sum::<f64>();
    sum_a.sqrt()
}

fn matrix_manhattan(matrix: &Vec<Vec<f64>>) -> f64 {
    matrix.iter().map(|row| row.iter().map(|a| a.abs()).sum::<f64>()).sum::<f64>()
}

fn matrix_max(matrix: &Vec<Vec<f64>>) -> f64 {
    matrix.iter()
        .map(
            |row| row.iter().map(|a| a.abs())
                .max_by(|a, b| a.partial_cmp(b).unwrap())
                .unwrap()
        ).max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap()
}

fn check_matrix(matrix: &Vec<Vec<f64>>) -> bool {
    matrix[0].len() == matrix.len()
}

fn check_matrices(matrix1: &Vec<Vec<f64>>, matrix2: &Vec<Vec<f64>>) -> bool {
    matrix1[0].len() == matrix2[0].len() && matrix1.len() == matrix2.len()
}

fn multiply_matrices(matrix1: &Vec<Vec<f64>>, matrix2: &Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    let rows_a = matrix1.len();
    let cols_a = matrix1[0].len();
    let cols_b = matrix2[0].len();

    let mut result: Vec<Vec<f64>> = vec![vec![0.0; cols_b]; rows_a];

    for i in 0..rows_a {
        for j in 0..cols_b {
            for k in 0..cols_a {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    result
}

struct Matrix {
    data: Vec<Vec<f64>>
}

impl Matrix {
    pub fn new(data: Vec<Vec<f64>>) -> Result<Matrix, ()> {
        if data.len() == 0 {
            println!("The matrix must contain at least one row.");
            return Err(());
        } else if data[0].len() == 0 {
            println!("The matrix must contain at least one column.");
            return Err(());
        }

        let col_length = data[0].len();

        for col in data.clone() {
            if col.len() != col_length {
                println!("The matrix's columns must be of the same size");
                return Err(());
            }
        }

        Ok(Matrix {
            data
        })
    }

    pub fn print(&self) {
        for row in &self.data {
            println!("{:?}", row);
        }
    }

    pub fn multiply_by_const(&mut self, x: f64) -> Matrix {
        let mut matrix = Matrix::new(self.data.clone()).unwrap();

        for i in 0..self.data.len() {
            for j in 0..self.data[i].len() {
                matrix.data[i][j] *= x;
            }
        }

        matrix
    }

    fn get_size(&self) -> (usize, usize) {
        (self.data.len(), self.data[0].len())
    }

    pub fn add(&mut self, other: Matrix) -> Result<Matrix, ()> {
        if self.get_size() != other.get_size() {
            println!("The matrices must be of the same size");
            return Err(());
        }

        let mut matrix = Matrix::new(self.data.clone())?;

        for i in 0..self.data.len() {
            for j in 0..self.data[i].len() {
                matrix.data[i][j] += other.data[i][j];
            }
        }

        Ok(matrix)
    }

    pub fn multiply(&mut self, other: Matrix) -> Result<Matrix, ()> {
        if self.get_size() != other.get_size() {
            println!("The matrices must be of the same size");
            return Err(());
        }

        Ok(Matrix::new(multiply_matrices(&self.data, &other.data))?)
    }
}

fn main() {
    let vec = vec![1.0, 2.0, 5.0];
    println!("Zad 1:");
    println!("{:?}", vec);
    println!("Norma euklidesowa: {}", euclidean_norm(&vec));
    println!("Norma Manhattan: {}", manhattan_norm(&vec));
    println!("Norma maksimum: {}", maximum_norm(&vec));

    println!();

    let (p, q) = ((5.0, 7.2), (2.0, 4.1));
    println!("Zad 2:");
    println!("Metryka euklidesowa: {}", euclidean_metric(p, q));
    println!("Metryka Manhattan: {}", manhattan_metric(p, q));
    println!("Metryka rzeki: {}", metryka_rzeki(p, q));
    println!("Metryka kolejowa: {}", metryka_kolejowa(p, q));

    println!();

    let matrix = vec![
        vec![2.0, 1.0],
        vec![3.0, 4.0]
    ];

    println!("Zad 3:");
    println!("{:?}", matrix);
    println!("{}", matrix_frobenius(&matrix));
    println!("{}", matrix_manhattan(&matrix));
    println!("{}", matrix_max(&matrix));

    println!();

    let matrix2 = vec![
        vec![2.0, 2.0],
        vec![4.0, 2.0]
    ];

    println!("Zad 4:");
    if check_matrices(&matrix, &matrix2) {
        let matrix3 = multiply_matrices(&matrix, &matrix2);
        println!("{:?}", matrix3);
    } else {
        println!("Nie można pomnożyć macierzy o nierównych rozmiarach")
    }

    println!();

    println!("Zad 5:");
    let mut matrix = Matrix::new(vec![
        vec![2.0, 2.0],
        vec![1.0, 4.0]
    ]).unwrap();
    let matrix2 = Matrix::new(vec![
        vec![1.0, 2.0],
        vec![4.0, 2.0]
    ]).unwrap();

    println!("Matrix 1:");
    matrix.print();
    println!();

    println!("Matrix 2:");
    matrix2.print();
    println!();

    let ones_matrix = Matrix::new(vec![
        vec![1.0, 1.0],
        vec![1.0, 1.0]
    ]).unwrap();

    let result = matrix.add(ones_matrix).unwrap();
    result.print();
    println!();

    let result = matrix.multiply_by_const(2.0);
    result.print();
    println!();

    let result = matrix.multiply(matrix2).unwrap();
    result.print();
}
