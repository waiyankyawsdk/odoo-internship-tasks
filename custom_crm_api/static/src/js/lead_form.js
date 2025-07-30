function submitLeadForm(event) {
    if (event) event.preventDefault();

    const token = '2cfc121d1adb22d2e1a0aa29503d7bc28a07c600';

    const nameInput = document.querySelector('#name');
    const emailInput = document.querySelector('#email');
    const phoneInput = document.querySelector('#phone');
    const descInput = document.querySelector('#description');


    if (!nameInput || !emailInput || !phoneInput || !descInput) {
        alert(' Input elements not found in the DOM. Please check the element IDs.');
        return;
    }

    const data = {
        name: nameInput.value.trim(),
        email: emailInput.value.trim(),
        phone: phoneInput.value.trim(),
        description: descInput.value.trim()
    };

    if (!data.name || !data.email || !data.phone) {
        alert(' Please fill in all required fields: name, email, and phone.');
        return;
    }

    console.log(" Sending data to server:", data);


    fetch('/api/create_lead', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    })
    .then(async res => {
        const contentType = res.headers.get('content-type');
        let jsonResponse = null;

        if (contentType && contentType.includes('application/json')) {
            jsonResponse = await res.json();
            console.log(' JSON response:', jsonResponse);
        }

        const isSuccess = jsonResponse?.result?.success === true;

        if (res.ok && isSuccess) {
            return jsonResponse;
        } else {
            const err = jsonResponse?.result?.error || 'Unknown error';
            throw new Error(err);
        }
    })
    .then(response => {
        console.log(' Full response from server:', response);

        const leadId =
            response.result?.lead?.id ||
            response.result?.id ||
            response.lead_id ||
            response.id ||
            null;

        if (leadId) {
            alert(' Lead created! ID: ' + leadId);

            setTimeout(() => {
            const form = document.getElementById('leadForm');
            if (form) form.reset();
            if (submitBtn) submitBtn.disabled = false;
            console.log(' Form cleared');
        }, 300);

            nameInput.value = '';
            emailInput.value = '';
            phoneInput.value = '';
            descInput.value = '';
            console.log(" Form cleared after alert OK");

        } else {
            alert(' Lead created, but ID not found.\n\nFull response:\n' + JSON.stringify(response, null, 2));
        }


        document.getElementById('leadForm')?.reset();
        console.log(" Form reset");
    })
    .catch(error => {
        let errorMsg = 'An unknown error occurred.';

        if (error instanceof Error) {
            errorMsg = error.message;
        } else if (typeof error === 'string') {
            errorMsg = error;
        } else if (typeof error === 'object' && error !== null) {
            errorMsg = error.error || error.message || JSON.stringify(error);
        }

        console.error(' Error caught:', error);
        alert(' Error: ' + errorMsg);
    });
}
