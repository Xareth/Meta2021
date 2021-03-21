import React, { useState } from "react";
import "./SideMenu.css";

function SideMenu(props) {

    return (<div className={props.isHidden ? "sideMenu sideMenu-hidden" : "sideMenu"}>
        <div className="sideMenu-close" onClick={props.SetHideSideMenu}><i className="fas fa-times"></i></div>
        <div className="sideMenu-moduls">
            <ul>
                <li>Salon nowe</li>
                <li>Salon używane</li>
                <li>Serwis</li>
                <li>BDC</li>
                <li>Recepcja</li>
                <li>Ustawienia</li>
            </ul>
        </div>
    </div>)
}

export default SideMenu;