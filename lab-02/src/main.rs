fn generate_vec(n: u32, m: u32) -> Vec<f32> {
    let mut vec = vec![];

    for k in 0..n {
        let a = 1.0 / ((k as f32 % m as f32 + 1.0) * (k as f32 % m as f32 + 2.0));
        vec.push(a)
    }

    vec
}

fn generate_vec_f64(n: u32, m: u32) -> Vec<f64> {
    let mut vec = vec![];

    for k in 0..n {
        let a = 1.0 / ((k as f64 % m as f64 + 1.0) * (k as f64 % m as f64 + 2.0));
        vec.push(a)
    }

    vec
}

fn sum_vec(vec: &Vec<f32>) -> f32 {
    vec.iter().sum()
}

fn sum_vec_f64(vec: &Vec<f64>) -> f64 {
    vec.iter().sum()
}

fn sum_gill_moller(n: u32, vec: &Vec<f32>) -> f32 {
    let mut sum = 0.0;
    let mut p = 0.0;
    let mut sum_old = 0.0;

    for i in 0..n {
        sum = sum_old + vec[i as usize];
        p = p + (vec[i as usize] - (sum - sum_old));
        sum_old = sum;
    }

    sum + p
}

fn sum_gill_moller_f64(n: u32, vec: &Vec<f64>) -> f64 {
    let mut sum = 0.0;
    let mut p = 0.0;
    let mut sum_old = 0.0;

    for i in 0..n {
        sum = sum_old + vec[i as usize];
        p = p + (vec[i as usize] - (sum - sum_old));
        sum_old = sum;
    }

    sum + p
}

fn sum_kahan(n: u32, vec: &Vec<f32>) -> f32 {
    let mut e = 0.0;
    let mut sum = 0.0;

    for i in 0..n {
        let temp = sum;
        let y = vec[i as usize] + e;
        sum = temp + y;
        e = (temp - sum) + y;
    }

    sum
}

fn sum_kahan_f64(n: u32, vec: &Vec<f64>) -> f64 {
    let mut e = 0.0;
    let mut sum = 0.0;

    for i in 0..n {
        let temp = sum;
        let y = vec[i as usize] + e;
        sum = temp + y;
        e = (temp - sum) + y;
    }

    sum
}

fn check_precision(n: u32, m: u32, sum: f32) -> f32 {
    let precise_sum = n as f32 / (m + 1) as f32;

    let absolute_error = (sum - precise_sum).abs() / precise_sum.abs();
    absolute_error
}

fn check_precision_f64(n: u32, m: u32, sum: f64) -> f64 {
    let precise_sum = n as f64 / (m + 1) as f64;

    let absolute_error = (sum - precise_sum).abs() / precise_sum.abs();
    absolute_error
}

fn main() {
    let n = 2_u32.pow(20);
    let m = 512;

    let vec = generate_vec(n, m);

    // println!("{:.12?}", vec);
    println!("{:.12}", n as f32 / (m + 1) as f32);

    println!(" ");

    println!("Normal sum:");
    println!("{:.12}", sum_vec(&vec));
    println!("{:e}", check_precision(n, m, sum_vec(&vec)));

    let sum_gill_moller = sum_gill_moller(n, &vec);
    println!("Gill-Moller sum:");
    println!("{:.12}", sum_gill_moller);
    println!("{:e}", check_precision(n, m, sum_gill_moller));

    let sum_kahan = sum_kahan(n, &vec);
    println!("Kahan sum:");
    println!("{:.12}", sum_kahan);
    println!("{:e}", check_precision(n, m, sum_kahan));

    println!(" ");

    let vec_f64 = generate_vec_f64(n, m);
    let sum_f64 = sum_vec_f64(&vec_f64);
    println!("{:.32}", sum_f64);
    println!("{:e}", check_precision_f64(n, m, sum_f64));

    let sum_gill_moller_f64 = sum_gill_moller_f64(n, &vec_f64);
    println!("Gill-Moller sum:");
    println!("{:.32}", sum_gill_moller_f64);
    println!("{:e}", check_precision_f64(n, m, sum_gill_moller_f64));

    let sum_kahan_f64 = sum_kahan_f64(n, &vec_f64);
    println!("Kahan sum:");
    println!("{:.32}", sum_kahan_f64);
    println!("{:e}", check_precision_f64(n, m, sum_kahan_f64));
}
