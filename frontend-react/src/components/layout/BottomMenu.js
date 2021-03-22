import React from "react";


function BottomMenu(props) {

    return (
        <div className="bottomMenu">
            {props.bottomMenuItems.map(CreateMenuItem)}
        </div>
    )
}

function CreateMenuItem(props) {
    return <MenuItem
        key={props}
        name={props}
     />
}

function MenuItem(props) {
    return <button className="button btn-botMenu">{props.name}</button>
}

export default BottomMenu;
