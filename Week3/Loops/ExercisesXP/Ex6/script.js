let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  for (let i in details) {
      console.log([i] + ' ' + details[i]);
  }

  //the sentence "my name is Rudolf the raindeer" appears but on 3 different lines. How to do it on one?