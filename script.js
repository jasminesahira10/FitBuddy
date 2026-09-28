function goPlanner() {

    document
        .getElementById("planner")
        .scrollIntoView({
            behavior: "smooth"
        });
}


function generatePlan() {

    const goal =
        document.getElementById("goal").value;

    const level =
        document.getElementById("level").value;

    const time =
        document.getElementById("time").value;

    const activity =
        document.getElementById("activity").value;

    const result =
        document.getElementById("result");


    result.innerHTML = `
        <p>🤖 Creating your personalized plan...</p>
    `;


    setTimeout(function () {

        let workout = "";

        if (activity === "Walking") {

            workout =
                "Start with a comfortable walk, followed by light stretching.";

        } else if (activity === "Yoga") {

            workout =
                "Begin with gentle yoga movements and finish with relaxed breathing.";

        } else if (activity === "Stretching") {

            workout =
                "Perform gentle full-body stretches without forcing any movement.";

        } else {

            workout =
                "Try simple bodyweight movements with comfortable intensity and proper rest.";

        }


        result.innerHTML = `

            <div class="plan-card">

                <h4>🎯 Goal</h4>
                <p>${goal}</p>

                <h4>📊 Level</h4>
                <p>${level}</p>

                <h4>⏱️ Time</h4>
                <p>${time}</p>

                <h4>🏃 Activity</h4>
                <p>${activity}</p>

                <h4>💪 Suggested Plan</h4>

                <p>
                    ${workout}
                </p>

                <h4>🌿 Healthy Habit</h4>

                <p>
                    Stay hydrated, take regular breaks,
                    and maintain a consistent sleep routine.
                </p>

                <h4>🤖 Gemini AI</h4>

                <p>
                    This interface is designed to connect
                    with a Gemini model for more personalized
                    AI-generated suggestions.
                </p>

            </div>

        `;

    }, 700);
}