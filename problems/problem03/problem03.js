function sort(a) {
    /* fill me in */
    return [];
}


function main() {
    let fs = require('fs');
    let stdin = fs.readFileSync(0).toString();
    let numbers = stdin.trim().split('\n').map(x => parseInt(x));
    let result = sort(numbers);
    for (x of result) {
        console.log(x);
    }
}

main();
