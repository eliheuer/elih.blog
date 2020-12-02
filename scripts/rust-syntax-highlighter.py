from pygments import highlight
from pygments.lexers import RustLexer
from pygments.formatters import HtmlFormatter

code = '''
use std::env;
use std::collections::HashMap;
use std::convert::TryInto;

fn main() {
    // Check for Roman numerals in command-line arguments
    let args: Vec<String> = env::args().collect();
    let mut arg_step = 1;
    let mut args_to_convert: Vec<i32> = Vec::new();
    // Note: the 0 arg is the command that ran the program, and is skipped
    for arg in &args[1..] {
        let mut roman_numeral = true;
        for character in arg.chars() {
            match character {
                'I' | 'V' | 'X' | 'L' | 'C' | 'D' | 'M' => (),
                _ => roman_numeral = false,
            }
        };
        if roman_numeral == true {
            args_to_convert.push(arg_step)
        };
        arg_step += 1
    };

    // Setup a key/value map for roman numeral values
    let roman_value: HashMap<char, i32> =
        [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
        .iter().cloned().collect();

    // Convert Roman numerals found in the previous process
    let mut title = args.to_vec();
    for index_number in args_to_convert {
        let arg_number: usize = index_number.try_into().unwrap();
        let arg_string = &title[arg_number];
        let arg_char_vec: Vec<char> = arg_string.chars().collect();
        let mut char_step = 0;
        let mut old_converted_number = 0;
        let mut new_converted_number = 0;
        let mut integer_value = 0;
        for roman_char in arg_char_vec {
            for (key, value) in roman_value.iter() {
                if roman_char == *key {
                    old_converted_number = new_converted_number;
                    new_converted_number = *value;
                }
            }
            if char_step > 0 && new_converted_number > old_converted_number {
                // Special case for the one-less-than strings like "IX" and "IV"
                // Note that with the string "IV", integer_value will be 1
                // going into the second loop, hence: 5 - (2 * 1) -> 5 - 1 -> 4
                integer_value += new_converted_number - 2 * old_converted_number
            } else {
                // Most conversions steps will use this
                integer_value += new_converted_number
            }
            char_step += 1;
        }
        let integer_value_string = integer_value.to_string();
        if integer_value_string == "1" {
            ();
        } else {
            title[arg_number] = integer_value_string;
        }
    }

    // Print the new title
    title.remove(0);
    let mut joined_title = title.join(" ");
    joined_title = joined_title.to_string();
    println!("{}", joined_title);
}
'''
print(highlight(code, RustLexer(), HtmlFormatter()))
print("--- END OUTPUT / START CSS ---")
#print(HtmlFormatter().get_style_defs('.highlight'))
