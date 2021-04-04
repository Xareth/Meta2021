import React, {useEffect} from "react";


// Render form operations (Update on change, After submit button)
function RenderForm(form, setForm, methods) {

    // Load form
    useEffect(() => {
        fetch(methods.route).then(response => response.json().then(data => {
            setForm(data.form)
        })).catch((e) => { console.log("Error occured: ",e) })
    }, []);


    // Update form on every change
    function UpdateOnChange(event) {
        const targetEvent = event.target;
        const { id, value } = targetEvent;
        let updatedForm = form;
        updatedForm[id].value = value;
        setForm(updatedForm);
        console.log(updatedForm);
    }


    // Action after submit button is pressed
    async function AfterFormSubmit(event) {

        event.preventDefault()

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            dataType: 'json',
            body: JSON.stringify(form)
        };
        const response = await fetch(methods.route, requestOptions);
        const result = await response.json();
        methods.setSubMod(result.route);
    }


    // Render form
    return (<div>
        <form onSubmit={AfterFormSubmit}>
            {form.length > 0 ? form.map((data) => { return <Input
                key={data.id}
                id={data.id}
                label={data.label}
                type={data.type}
                field={data.field}
                update={UpdateOnChange}
            />  }) : ""}
        </form>
    </div>)
}


function Input(props) {
    return <div>
        <label>{props.label}</label>
        <input id={props.id} type={props.type} onChange={props.update} name={props.label} />
    </div>
}

export default RenderForm;