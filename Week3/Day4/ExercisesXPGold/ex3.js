let verb = prompt('Please, write any verb');
if (verb.length >= 3 && verb.slice(verb.length - 3) != "ing") {
    alert(verb + "ing");
} else if (verb.length >= 3 && verb.slice(verb.length - 3) === "ing") {
    alert(verb + "ly");

} else {
    alert(verb);
}