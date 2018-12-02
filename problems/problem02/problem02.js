function reverse(s) {
    /* fill me in */
    return "TODO";
}


function main() {
    let fs = require('fs');
    let stdin = fs.readFileSync(0).toString();
    let lines = stdin.trim().split('\n');
    let result = reverse(lines[0]);
    console.log(result);
}

main();
