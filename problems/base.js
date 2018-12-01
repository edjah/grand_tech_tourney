function func() {
    /* fill me in */
}



function main() {
    let fs = require('fs');
    let stdin = fs.readFileSync(0).toString();
    let lines = stdin.trim().split('\n');
    // let numbers = lines.map(x => parseInt(x));
    let result = func(lines);
    console.log(result);
}
