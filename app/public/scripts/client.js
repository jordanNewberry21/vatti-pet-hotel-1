$(function () {
  //on ready func using anonymous function
});

function renderPets(petData) {
  let display = $('#placeHolder');
  display.empty();
  for (pet of petData) {
    let $tr = $(`<tr data-id='${pet.id}'</tr>`);
    $tr.data('pet', pet);
    $tr.append(`<td class="name" data-name='${pet.name}'>${pet.name}</td>`);
    $tr.append(`<td class="breed">${pet.breed}</td>`);
    $tr.append(`<td class="color">${pet.color}</td>`);
    $tr.append(
      `<td class="checkIn" data-checkIn='${pet.checkIn}'>${pet.checkIn}</td>`
    );
    $tr.append(`<td class="notes">${pet.notes}</td>`);
    $tr.append(
      `<td class="td-checkIn"><button class='btn-checkIn'>Mark For checkIn</button></td>`
    );
    $tr.append(
      `<td class="td-delete"><button class='btn-delete'>Delete</button></td>`
    );
    display.append($tr);
  }
}
