import React from "react";


function BottomMenu(props) {

    return (
        <div className="bottomMenu" onClick={props.SetCloseSideMenu}>
            {props.bottomMenuItems.map((data) => {
                return <MenuItem
                    key={data}
                    name={data}
                    SetSubMod={props.SetSubModule}
                    subMod={props.subMod}
                />
            })}
        </div>
    )
}

function MenuItem(props) {
    return <button onClick={props.SetSubMod} name={props.name}
                   className={ props.subMod === props.name ? "button btn-botMenu btn-botMenu-active" : "button btn-botMenu" }
    >{props.name}</button>
}

export default BottomMenu;
