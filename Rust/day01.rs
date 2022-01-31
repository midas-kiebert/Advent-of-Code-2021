use std::fs::File;
use std::io::prelude::*;

fn count_increases(list: &Vec<&str>, window: usize) -> i32 {
    let mut increasing = 0;
    for i in window..list.len()-window {
        if list[i].parse::<i32>().unwrap() > list[i-window].parse::<i32>().unwrap() {
            increasing += 1;
        }
    }
    increasing
}

fn main() {
    let mut file = File::open("../inputs/day01.txt").unwrap();
    let mut input = String::new();
    file.read_to_string(&mut input).unwrap();
    let list: Vec<&str> = input.split('\n').collect();

    println!("{}", count_increases(&list, 1));
    println!("{}", count_increases(&list, 3));
}