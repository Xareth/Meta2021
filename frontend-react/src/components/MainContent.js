import React, {useState} from "react";
import Login from "./users/Login";
import Settings from "./settings/Settings";


function MainContent(props) {

    return <div className="container-content">
        {props.module === "login" ? <Login SetBottomMenu={props.SetBottomMenu} /> : ""}
        {props.module === "salon-nowe" ? <Settings SetBottomMenu={props.SetBottomMenu} /> : ""}
        {props.module === "salon-uzywane" ? <Login SetBottomMenu={props.SetBottomMenu} /> : ""}
    </div>
}

export default MainContent;