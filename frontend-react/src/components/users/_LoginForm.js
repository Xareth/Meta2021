import React, { useEffect, useState } from "react";
import RenderForm from "../forms/FormHandler";


function _LoginForm(props) {

    const [ loginForm, setLoginForm ] = useState([]);

    // Render form
    return RenderForm(loginForm, setLoginForm)
}


export default _LoginForm;