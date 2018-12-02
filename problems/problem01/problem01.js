function search(a, i) {
    /* fill me in */
}



function main() {
    let fs = require('fs');
    let stdin = fs.readFileSync(0).toString();
    let lines = stdin.trim().split('\n');
    let numbers = lines.map(x => parseInt(x));
    let search_value = numbers.pop();
    let result = search(numbers, search_value);
    console.log(result);
}

main();
