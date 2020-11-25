console.log('isadhfsahjfaf');

$(function () {
  console.log('in ready function');
  getPets();
  //on ready func using anonymous function

});


function getPets() { // ajax GET function
  $.ajax({
    method: 'GET',
    url: '/pets' // setting the url for data transactions
  }).then(function (response) {
    console.log(response);
    renderPets(response); // call render with response from server
  }).catch(function (error) {
    console.log('error in GET route', error);
  });
};


function renderPets(petData) {
  let display = $('#petTables');
  display.empty();
  console.log('petData is...', petData[0].name);
  // for (pet of petData) {
  //   let $tr = $(`<tr data-id='${pet.id}'</tr>`);
  //   $tr.data('pet', pet);
  //   $tr.append(`<td class="name" data-name='${pet.name}'>${pet.name}</td>`);
  //   $tr.append(`<td class="breed">${pet.breed}</td>`);
  //   $tr.append(`<td class="color">${pet.color}</td>`);
  //   $tr.append(
  //     `<td class="checkIn" data-checkIn='${pet.checked_in}'>${pet.checked_in}</td>`
  //   );
  //   $tr.append(`<td class="notes">${pet.notes}</td>`);
  //   $tr.append(
  //     `<td class="td-checkIn"><button class='btn-checkIn'>Mark For checkIn</button></td>`
  //   );
  //   $tr.append(
  //     `<td class="td-delete"><button class='btn-delete'>Delete</button></td>`
  //   );
  //   display.append($tr);
  // }
}