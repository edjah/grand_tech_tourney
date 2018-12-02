function two_sum(a, target) {
    /* fill me in */
}


function main() {
    let fs = require('fs');
    let stdin = fs.readFileSync(0).toString();
    let lines = stdin.trim().split('\n');
    let numbers = lines.map(x => parseInt(x));
    let search_value = numbers.pop();
    let result = two_sum(numbers, search_value);
    console.log(result);
}

main();
