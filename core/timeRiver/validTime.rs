/*
Check if the given string is a correct time representation of the 24-hour clock.

Example

  For time = "13:58", the output should be
    validTime(time) = true;
  
  For time = "25:51", the output should be
    validTime(time) = false;
  
  For time = "02:76", the output should be
    validTime(time) = false.

*/

fn validTime(time: String) -> bool {
  let mut x = time.clone();
  
  let mins = x.split_off(3).parse::<u32>().unwrap();
  let hrs = x.trim_end_matches(':').parse::<u32>().unwrap();
  
  match (hrs, mins) {
    (0..=23, 0..=59) => true,
    _ => false,
  }
  
}
