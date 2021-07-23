let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[2] = "Jason";
people.push("Liza");
for (let i in people) {
    if ( i = "Jason") {
        break
    }
    console.log(people[i]);
}
