let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[3] = "Jason";
people.push("Liza");
for (let i in people) {
    console.log(people[i]);
}
