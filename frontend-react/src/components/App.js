import React, { useEffect, useState } from "react";
import BottomMenu from "./layout/BottomMenu";
import SideMenu from "./layout/SideMenu";
import TopNavigation from "./layout/TopNavigation";
import MainContent from "./MainContent";

function App() {
    const [ isHidden, setHidden ] = useState(true);
    const [ bottomMenuItems, setBottomMenuItems ] = useState([]);
    const [ module, setModule ] = useState("login");
    const [ subMod, setSubMod ] = useState("");

    // Hides side menu
    function SetHideSideMenu(event) {
        setHidden(!isHidden);
    }

    function SetCloseSideMenu(event) {
        setHidden(true);
    }

    // Generates items in bottom menu
    function SetBottomMenu(event) {
        setBottomMenuItems(event);
    }

    // Sets name of current module
    function SetModuleName(event) {
        setModule(event.target.attributes[0].nodeValue);
        setSubMod("");
        SetCloseSideMenu();
    }

    // Sets the name of the submodule
    function SetSubModule(event) {
        setSubMod(event.target.attributes[0].value);
    }

    // Renders 4 main website components
    return <div className="container container-main">
        <TopNavigation
            SetHideSideMenu={SetHideSideMenu}
            SetCloseSideMenu={SetCloseSideMenu}
        />
        <MainContent
            SetBottomMenu={SetBottomMenu}
            module={module}
            subMod={subMod}
            SetCloseSideMenu={SetCloseSideMenu}
        />
        <BottomMenu
            bottomMenuItems={bottomMenuItems}
            SetSubModule={SetSubModule}
            subMod={subMod}
            SetCloseSideMenu={SetCloseSideMenu}
        />
        <SideMenu
            SetHideSideMenu={SetHideSideMenu}
            SetModuleName={SetModuleName}
            isHidden={isHidden}
        />
    </div>
}

export default App;
