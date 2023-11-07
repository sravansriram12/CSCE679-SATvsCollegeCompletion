
  
const statesDropdown = document.getElementById("states");
const compareStateDropdown = document.getElementById("statescompare");

const stateSubmit = document.getElementById("submitstate");


statesDropdown.addEventListener("change", () => {
  stateSubmit.disabled = false;
})

compareStateDropdown.addEventListener("change", () => {
  stateSubmit.disabled = false;
})