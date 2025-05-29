const prompt = require('prompt-sync')();  // ← import prompt-sync

function is_palindrom(word){
    console.log('word is : ', word)
    for (let i=0; i < Math.floor(word.length) /2; i++){
        console.log(i)
        if (word[i] !== word[word.length - i - 1]) {
                return false;
            }
        }
    return true;
}

const word = prompt("enter word : ")
if (is_palindrom(word)){
    console.log('yes palindrom')
}
else{
    console.log('false')
}