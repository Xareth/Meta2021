import React from "react";
import "./TopNavigation.css";

function TopNavigation(props) {
    return (<div className="topNavigation">
        <div className="tn-right">
            <p onClick={props.SetHideSideMenu}><i className="fas fa-bars"></i></p>
        </div>
        <div className="tn-logo">
            <div><img src="static/base/MotortestLogoPoziome.png" alt="logo" /></div>
        </div>
        <div className="tn-mid">
            <div className="tn-mid-long">
                <span> Home </span>
                <i className="fas fa-angle-right"></i><span> Settings </span>
                <i className="fas fa-angle-right"></i><span> Roles </span>
            </div>
            <div className="tn-mid-short">
                <span> Roles </span>
            </div>
        </div>

    </div>)
}


export default TopNavigation;