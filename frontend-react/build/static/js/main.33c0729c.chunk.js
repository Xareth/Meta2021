(this["webpackJsonpfrontend-react"]=this["webpackJsonpfrontend-react"]||[]).push([[0],{10:function(e,t,n){},12:function(e,t,n){"use strict";n.r(t);var c=n(1),s=n.n(c),o=n(4),i=n.n(o),a=(n(9),n(10),n(2)),u=n(0);function r(e){return Object(u.jsx)("button",{onClick:e.SetSubMod,name:e.name,className:e.subMod===e.name?"button btn-botMenu btn-botMenu-active":"button btn-botMenu",children:e.name})}var d=function(e){return Object(u.jsx)("div",{className:"bottomMenu",onClick:e.SetCloseSideMenu,children:e.bottomMenuItems.map((function(t){return Object(u.jsx)(r,{name:t,SetSubMod:e.SetSubModule,subMod:e.subMod},t)}))})};function j(e){return Object(u.jsx)("li",{name:e.route,onClick:e.setModuleName,children:e.name})}var l=function(e){var t=Object(c.useState)([{name:"login",route:"login"},{name:"ustawienia",route:"settings"}]),n=Object(a.a)(t,2),s=n[0];return n[1],Object(u.jsxs)("div",{className:e.isHidden?"sideMenu sideMenu-hidden":"sideMenu",children:[Object(u.jsx)("div",{className:"sideMenu-close",onClick:e.SetHideSideMenu,children:Object(u.jsx)("i",{className:"fas fa-times"})}),Object(u.jsx)("div",{className:"sideMenu-moduls",children:Object(u.jsx)("ul",{children:s.map((function(t){return Object(u.jsx)(j,{name:t.name,route:t.route,setModuleName:e.SetModuleName},t.name)}))})})]})};var b=function(e){return Object(u.jsxs)("div",{className:"topNavigation",children:[Object(u.jsx)("div",{className:"tn-right",children:Object(u.jsx)("p",{onClick:e.SetHideSideMenu,children:Object(u.jsx)("i",{className:"fas fa-bars"})})}),Object(u.jsx)("div",{className:"tn-logo",children:Object(u.jsx)("div",{children:Object(u.jsx)("img",{src:"static/base/MotortestLogoPoziome.png",alt:"logo"})})}),Object(u.jsxs)("div",{className:"tn-mid",children:[Object(u.jsxs)("div",{className:"tn-mid-long",children:[Object(u.jsx)("span",{children:" Home "}),Object(u.jsx)("i",{className:"fas fa-angle-right"}),Object(u.jsx)("span",{children:" Settings "}),Object(u.jsx)("i",{className:"fas fa-angle-right"}),Object(u.jsx)("span",{children:" Roles "})]}),Object(u.jsx)("div",{className:"tn-mid-short",children:Object(u.jsx)("span",{children:" Roles "})})]})]})};var m=function(e){return Object(u.jsx)("div",{children:"Login Form"})};var O=function(e){var t=["Login","whatever"];return Object(c.useEffect)((function(){e.SetBottomMenu(t),fetch("/_users").then((function(e){return e.json().then((function(e){console.log(e)}))})).catch((function(e){console.log("Error occured: ",e)}))}),[]),Object(u.jsx)("div",{children:"Login"===e.subMod?Object(u.jsx)(m,{}):""})};var M=function(e){var t=["Set","Ings"];return Object(c.useEffect)((function(){e.SetBottomMenu(t)}),[]),Object(u.jsx)("div",{children:"Login"})};var S=function(e){return Object(u.jsxs)("div",{id:"main-content",className:"container-content",children:["login"===e.module?Object(u.jsx)(O,{SetBottomMenu:e.SetBottomMenu,SubMod:e.subMod}):"","settings"===e.module?Object(u.jsx)(M,{SetBottomMenu:e.SetBottomMenu}):""]})};var f=function(){var e=Object(c.useState)(!0),t=Object(a.a)(e,2),n=t[0],s=t[1],o=Object(c.useState)([]),i=Object(a.a)(o,2),r=i[0],j=i[1],m=Object(c.useState)("login"),O=Object(a.a)(m,2),M=O[0],f=O[1],x=Object(c.useState)(""),h=Object(a.a)(x,2),v=h[0],g=h[1];function N(e){s(!n)}function p(e){s(!0)}return Object(u.jsxs)("div",{className:"container container-main",children:[Object(u.jsx)(b,{SetHideSideMenu:N,SetCloseSideMenu:p}),Object(u.jsx)(S,{SetBottomMenu:function(e){j(e)},module:M,subMod:v,SetCloseSideMenu:p}),Object(u.jsx)(d,{bottomMenuItems:r,SetSubModule:function(e){g(e.target.attributes[0].value),console.log("SetSubModule called: ",e.target.attributes[0].value),console.log("SubMod:",v)},subMod:v,SetCloseSideMenu:p}),Object(u.jsx)(l,{SetHideSideMenu:N,SetModuleName:function(e){f(e.target.attributes[0].nodeValue)},isHidden:n})]})};i.a.render(Object(u.jsx)(s.a.StrictMode,{children:Object(u.jsx)(f,{})}),document.getElementById("root"))},9:function(e,t,n){}},[[12,1,2]]]);
//# sourceMappingURL=main.33c0729c.chunk.js.map