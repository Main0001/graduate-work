function handleSearchInputVillages(value) {
  const options = document.querySelectorAll("#villageslist option");
  for (let i = 0; i < options.length; i++) {
    if (options[i].value === value) {
      window.location.href = options[i].getAttribute("data-link");
      break;
    }
  }
}

function handleSearchInputEvents(value) {
  const options = document.querySelectorAll("#eventslist option");
  for (let i = 0; i < options.length; i++) {
    if (options[i].value === value) {
      window.location.href = options[i].getAttribute("data-link");
      break;
    }
  }
}
