window.addEventListener("load", () => {
    const sportSelect  = document.getElementById("sport-selection");
    let   sportOptions = [];

    for (const sportOption of sportSelect) {
        sportOptions.push(sportOption.value);
    }
    
    sportSelect.addEventListener("change", () => {
        for (const sport of sportOptions){
            if (sport != sportSelect.value && sportSelect.value != "todos"){
                const sportDivs = document.getElementsByName(sport);
                for (const div of sportDivs){
                    div.style.display = "none";
                }
            } else {
                const sportDivs = document.getElementsByName(sport);
                for (const div of sportDivs){
                    div.style.display = "";
                }
            }
        }
    });


    const minDateChoice = document.getElementById("date-min-choice");
    const maxDateChoice = document.getElementById("date-max-choice");
    
    minDateChoice.addEventListener("change", () => {
        const minDate = minDateChoice.value.split('-').join('');
        const maxDate = maxDateChoice.value.split('-').join('');

        const eventInfos = document.getElementsByName("event-info");
        for (const event of eventInfos){
            const eventDate = event.getAttribute('data-date');
            if (eventDate >= minDate && eventDate <= maxDate){
                event.style.display = "";
            } else {
                event.style.display = "none";
            }
        }
    });


    maxDateChoice.addEventListener("change", () => {
        const maxDate = maxDateChoice.value.split('-').join('');
        const minDate = minDateChoice.value.split('-').join('');

        const eventInfos = document.getElementsByName("event-info");
        for (const event of eventInfos){
            const eventDate = event.getAttribute('data-date');
            if (eventDate >= minDate && eventDate <= maxDate){
                event.style.display = "";
            } else {
                event.style.display = "none";
            }
        }
    });
});