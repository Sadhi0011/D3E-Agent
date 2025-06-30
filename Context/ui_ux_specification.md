Style {
    name 'Bootstrap'
    items [
        {
            selector 'TextView.h1'
            values {
                fontSize '36'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.h2'
            values {
                fontSize '30'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.h3'
            values {
                fontSize '24'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.h4'
            values {
                fontSize '18'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.h5'
            values {
                fontSize '14'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.h6'
            values {
                fontSize '12'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingOne'
            values {
                fontSize '36'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingTwo'
            values {
                fontSize '30'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingThree'
            values {
                fontSize '24'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingFour'
            values {
                fontSize '18'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingFive'
            values {
                fontSize '14'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.headingSix'
            values {
                fontSize '12'
                fontWeight 'bold'
                margin '20 0 10 0'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.dh1'
            values {
                fontSize '60.0'
                margin '10 0 10 0'
            }
        }
        {
            selector 'TextView.dh2'
            values {
                fontSize '50.0'
                margin '10 0 10 0'
            }
        }
        {
            selector 'TextView.dh3'
            values {
                fontSize '40.0'
                margin '10 0 10 0'
            }
        }
        {
            selector 'TextView.dh4'
            values {
                fontSize '30.0'
                margin '10 0 10 0'
            }
        }
        {
            selector 'TextView.lead'
            values {
                fontSize '21'
                fontWeight 'w300'
                margin '20 0 10 0'
            }
        }
        {
            selector 'TextView.small'
            values {
                fontSize '12'
                fontWeight 'w300'
                margin '20 0 10 0'
            }
        }
        {
            selector 'TextView.delete'
            values {
                textDecoration 'lineThrough'
            }
        }
        {
            selector 'TextView.strike'
            values {
                textDecoration 'lineThrough'
            }
        }
        {
            selector 'TextView.insert'
            values {
                textDecoration 'underline'
            }
        }
        {
            selector 'TextView.underline'
            values {
                textDecoration 'underline'
            }
        }
        {
            selector 'TextView.strong'
            values {
                fontWeight 'w700'
            }
        }
        {
            selector 'TextView.em'
            values {
                fontStyle 'italic'
            }
        }
        {
            selector 'TextView.textleft'
            values {
                textAlign 'left'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.textcenter'
            values {
                textAlign 'center'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.textright'
            values {
                textAlign 'right'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.textjustify'
            values {
                textAlign 'justify'
                softWrap 'true'
            }
        }
        {
            selector 'TextView.abbr'
            values {
                decorationStyle 'dotted'
                softWrap 'true'
                textDecoration 'underline'
            }
        }
        {
            selector 'TextView.blockquote'
            values {
                padding '10 20'
                margin '0 0 20 0'
                fontSize '17.5'
                decoration {
                    border {
                        left {
                            color '@c4'
                            width '5.0'
                            style 'solid'
                        }
                    }
                }
            }
        }
        {
            selector 'TextView.muted'
            values {
                color '@c6'
            }
        }
        {
            selector 'TextView.primary'
            values {
                color '@c15'
            }
        }
        {
            selector 'TextView.success'
            values {
                color '@c19'
            }
        }
        {
            selector 'TextView.info'
            values {
                color '@c23'
            }
        }
        {
            selector 'TextView.warning'
            values {
                color '@c27'
            }
        }
        {
            selector 'TextView.danger'
            values {
                color '@c31'
            }
        }
        {
            selector 'BasicSideBarView Column'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c3'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'BasicSideBarView Column.profile'
            values {
                width '50'
                height '50'
                decoration {
                    borderRadius '25'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'BasicDropdown Row'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1.0'
                    }
                    borderRadius '3'
                }
                padding '5 10'
            }
        }
        {
            selector 'BasicDropdownPopup ListView'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1.0'
                    }
                }
            }
        }
        {
            selector 'BasicDropdownPopup Row:hover'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'CollapsibleSideMenu'
            values {
                decoration {
                    color '@c3'
                }
            }
        }
        {
            selector 'CollapseSideMenuButton Row'
            values {
                textStyle {
                    color '@c2'
                    fontSize '16'
                    fontWeight 'w600'
                }
            }
        }
        {
            selector 'CollapseSideMenuButton Row:hover'
            values {
                decoration {
                    color '@c12'
                }
                textStyle {
                    color '@c13'
                    fontSize '16'
                    fontWeight 'w600'
                }
            }
        }
        {
            selector 'CollapseSideMenuButton Row:selected'
            values {
                decoration {
                    color '@c10'
                }
                textStyle {
                    fontSize '16'
                    fontWeight 'w600'
                    color '@c11'
                }
            }
        }
         {
            selector 'AppBar TextView'
            values {
                color '@c1'
            }
        }
        {
            selector 'AppBar IconView'
            values {
                color '@c1'
            }
        }
        {
            selector 'Button'
            values {
                padding '6 12'
                decoration {
                    color '@c5'
                    border {
                        width '1'
                        color '@c3'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'Button.rounded'
            values {
                padding '0 0'
                height '42'
                width '42'
                textStyle {
                    color '@c9'
                }
                decoration {
                    color '@c15'
                    border {
                        color '@c14'
                        width '1'
                    }
                    borderRadius '21'
                }
            }
        }
        {
            selector 'Button.roundedOutline'
            values {
                padding '0 0'
                height '42'
                width '42'
                textStyle {
                    color '@c15'
                }
                decoration {
                    color '@c1'
                    border {
                        color '@c14'
                        width '1'
                    }
                    borderRadius '21'
                }
            }
        }
        {
            selector 'Button.default'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c3'
                    }
                    borderRadius '4'
                }
                padding '6 12'
            }
        }
        {
            selector 'Button.default:hover'
            values {
                decoration {
                    color '@c5'
                    border {
                        width '1'
                        color '@c6'
                    }
                    borderRadius '4'
                }
                padding '6 12'
            }
        }
        {
            selector 'Button.primary'
            values {
                decoration {
                    color '@c15'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.primary:hover'
            values {
                decoration {
                    color '@c16'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.success'
            values {
                decoration {
                    color '@c19'
                    border {
                        width '1'
                        color '@c18'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.success:hover'
            values {
                decoration {
                    color '@c20'
                    border {
                        width '1'
                        color '@c18'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.info'
            values {
                decoration {
                    color '@c23'
                    border {
                        width '1'
                        color '@c22'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.info:hover'
            values {
                decoration {
                    color '@c24'
                    border {
                        width '1'
                        color '@c22'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.warning'
            values {
                decoration {
                    color '@c27'
                    border {
                        width '1'
                        color '@c26'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.warning:hover'
            values {
                decoration {
                    color '@c28'
                    border {
                        width '1'
                        color '@c26'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.danger'
            values {
                decoration {
                    color '@c31'
                    border {
                        width '1'
                        color '@c30'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.primaryOutline'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c15'
                }
            }
        }
        {
            selector 'Button.primaryOutline:hover'
            values {
                decoration {
                    color '@c15'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.successOutline'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c18'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c19'
                }
            }
        }
        {
            selector 'Button.successOutline:hover'
            values {
                decoration {
                    color '@c19'
                    border {
                        width '1'
                        color '@c18'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.infoOutline'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c22'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c23'
                }
            }
        }
        {
            selector 'Button.infoOutline:hover'
            values {
                decoration {
                    color '@c24'
                    border {
                        width '1'
                        color '@c22'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.warningOutline'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c26'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c27'
                }
            }
        }
        {
            selector 'Button.warningOutline:hover'
            values {
                decoration {
                    color '@c27'
                    border {
                        width '1'
                        color '@c26'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.dangerOutline'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c30'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c31'
                }
            }
        }
        {
            selector 'Button.dangerOutline:hover'
            values {
                decoration {
                    color '@c31'
                    border {
                        width '1'
                        color '@c30'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.large'
            values {
                padding '10 16'
            }
        }
        {
            selector 'Button.large:hover'
            values {
                padding '10 16'
            }
        }
        {
            selector 'Button.danger:hover'
            values {
                decoration {
                    color '@c32'
                    border {
                        width '1'
                        color '@c30'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.link'
            values {
                decoration {
                    color '00ff0000'
                    border {
                        width '0'
                        color '00ff0000'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c15'
                }
            }
        }
        {
            selector 'Button.link:hover'
            values {
                decoration {
                    color '00ff0000'
                    border {
                        width '0'
                        color '00ff0000'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c15'
                    decoration 'underline'
                }
            }
        }
        {
            selector 'Button.small'
            values {
                padding '5 10'
            }
        }
        {
            selector 'Button.small:hover'
            values {
                padding '5 10'
            }
        }
        {
            selector 'Button.xsmall'
            values {
                padding '1 5'
            }
        }
        {
            selector 'Button.xsmall:hover'
            values {
                padding '1 5'
            }
        }
        {
            selector 'Button.block'
            values {
                expand 'true'
                decoration {
                    color '@c15'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.block:hover'
            values {
                expand 'true'
                decoration {
                    color '@c16'
                    border {
                        width '1'
                        color '@c14'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Button.nav'
            values {
                decoration {
                    color '@c1'
                    border {
                        width '1'
                        color '@c4'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                margin '8 0'
            }
        }
        {
            selector 'Button.nav:hover'
            values {
                decoration {
                    color '@c5'
                    border {
                        width '1'
                        color '@c6'
                    }
                    borderRadius '4'
                }
                padding '6 12'
                margin '8 0'
            }
        }
        {
            selector 'Button.SideMenuButton'
            values {
                decoration {
                    borderRadius '3'
                    color '@c5'
                }
                textStyle {
                    fontSize '16'
                    fontWeight 'w600'
                    color '@c2'
                }
            }
        }
        {
            selector 'Button.SideMenuButton:hover'
            values {
                decoration {
                    color '@c12'
                    borderRadius '3'
                }
                textStyle {
                    color '@c13'
                }
            }
        }
        {
            selector 'Button.SideMenuButton:selected'
            values {
                decoration {
                    color '@c10'
                    borderRadius '3'
                }
                textStyle {
                    color '@c11'
                }
            }
        }
        {
            selector 'Chip Button'
            values {
                padding '0'
                decoration {
                    color '@c1'
                    borderRadius '0'
                    border {
                        color '@c9'
                        width '0.0'
                    }
                }
            }
        }
        {
            selector 'TextIconButton Row'
            values {
                mainAxisSize 'min'
            }
        }
        {
            selector 'TextIconButton.appart Row'
            values {
                mainAxisSize 'max'
                mainAxisAlignment 'spaceBetween'
            }
        }
        {
            selector 'TextIconButton.roundIcon IconView'
            values {
                padding '7'
                decoration {
                    border {
                        width '1'
                    }
                    borderRadius '30'
                }
            }
        }
        {
            selector 'Checkbox'
            values {
                height '18'
                width '18'
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '1'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'Checkbox.rounded'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '1'
                    }
                    borderRadius '10'
                }
            }
        }
        {
            selector 'Checkbox.rounded:active'
            values {
                decoration {
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                    borderRadius '10'
                }
            }
        }
        {
            selector 'Checkbox:active'
            values {
                decoration {
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'Checkbox IconView'
            values {
                color '@c1'
                size '14'
            }
        }
        {
            selector 'Checkbox:disabled'
            values {
                decoration {
                    color '@c5'
                    border {
                        color '@c5'
                        width '1'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'Checkbox IconView.disabled'
            values {
                color '@c5'
                size '14'
            }
        }
        {
            selector 'Checkbox:focus'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c8'
                        width '1'
                    }
                    boxShadow {
                        color '@c15'
                        blurRadius '3'
                        spreadRadius '3'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'IconCheckbox'
            values {
                height '44'
                width '44'
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '2'
                    }
                    borderRadius '30'
                }
            }
        }
        {
            selector 'IconCheckbox Container.rounded'
            values {
                height '28'
                width '58'
                decoration {
                    borderRadius '15'
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'IconCheckbox:active'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c15'
                        width '2'
                    }
                    borderRadius '30'
                }
                textStyle {
                    color '@c15'
                }
            }
        }
        {
            selector 'IconCheckbox:focus'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c8'
                        width '2'
                    }
                    boxShadow {
                        color '@c15'
                        blurRadius '3'
                        spreadRadius '3'
                    }
                    borderRadius '30'
                }
            }
        }
        {
            selector 'TextCheckbox'
            values {
                height '32'
                width '64'
                decoration {
                    color '@c7'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TextCheckbox:active'
            values {
                decoration {
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TextCheckbox:focus'
            values {
                decoration {
                    color '@c8'
                    border {
                        color '@c8'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'CardCheckbox'
            values {
                padding '5'
                height '112'
                width '112'
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '1'
                    }
                    borderRadius '6'
                }
            }
        }
        {
            selector 'CardCheckbox:active'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c15'
                        width '1'
                    }
                    borderRadius '6'
                }
            }
        }
        {
            selector 'Toggle'
            values {
                textStyle {
                    color '@c9'
                }
                padding '3'
                height '24'
                width '50'
                decoration {
                    borderRadius '12'
                    color '@c7'
                }
            }
        }
        {
            selector 'Toggle TextView'
            values {
                padding '0 5'
            }
        }
        {
            selector 'Toggle:active'
            values {
                decoration {
                    borderRadius '13'
                    color '@c15'
                }
            }
        }
        {
            selector 'Toggle Container.round'
            values {
                height '16'
                width '16'
                decoration {
                    borderRadius '8'
                    color '@c9'
                }
            }
        }
        {
            selector 'Toggle.outer'
            values {
                margin '0'
            }
        }
        {
            selector 'Toggle.outer Container.round'
            values {
                height '24'
                width '24'
                decoration {
                    borderRadius '12'
                    color '@c9'
                }
            }
        }
        {
            selector 'IconToggle Container.body'
            values {
                height '28'
                width '58'
                decoration {
                    borderRadius '15'
                    color '@c7'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'IconToggle Container.body:active'
            values {
                decoration {
                    borderRadius '15'
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'IconToggle'
            values {
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'StatusToggle'
            values {
                margin '5'
            }
        }
        {
            selector 'StatusToggle Container.rounded'
            values {
                height '20'
                width '42'
                decoration {
                    borderRadius '10'
                    color '@c15'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'StatusToggle Container.roundedBox'
            values {
                height '14'
                width '14'
                decoration {
                    borderRadius '7'
                    color '@c9'
                }
            }
        }
        {
            selector 'StatusCheckbox TextView'
            values {
                color '@c15'
                fontSize '14'
                fontWeight 'w400'
            }
        }
        {
            selector 'CheckboxWithText'
            values {
                height '18'
                width '18'
                margin '4 15 0 0'
            }
        }
        {
            selector 'TextWithCheckbox'
            values {
                height '18'
                width '18'
            }
        }
        {
            selector 'ToggleBase'
            values {
                decoration {
                    border {
                        color '@c7'
                        width '1'
                    }
                    color '@c1'
                    borderRadius '4'
                }
            }
        }
        {
            selector 'ToggleBase Container:active'
            values {
                textStyle {
                    color '@c9'
                }
                decoration {
                    border {
                        color '@c15'
                        width '1'
                    }
                    color '@c15'
                }
            }
        }
        {
            selector 'SwitchToggle TextView'
            values {
                padding '0 5'
            }
        }
        {
            selector 'SwitchToggle Container:active'
            values {
                decoration {
                    color '@c15'
                    border {
                        color '@c15'
                        width '1'
                    }
                    borderRadius '12'
                }
            }
        }
        {
            selector 'SwitchToggle Container'
            values {
                margin '2.0'
            }
        }
        {
            selector 'SwitchToggle ToggleBase'
            values {
                padding '2'
                decoration {
                    border {
                        color '@c15'
                        width '1'
                    }
                    color '@c1'
                    borderRadius '12'
                }
            }
        }
        {
            selector 'SwitchStatus Container:active'
            values {
                decoration {
                    color '@c15'
                    border {
                        color '@c15'
                    }
                    borderRadius '30'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Table'
            values {
                defaultColumnWidth '1.flex'
                defaultVerticalAlignment 'middle'
                border {
                    top {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    bottom {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    horizontalInside {
                        color '@c7'
                        width '1'
                        style 'solid'
                    }
                }
            }
        }
        {
            selector 'TableRow'
            values {
                decoration {
                    color '@c1'
                }
                textStyle {
                    color '@c2'
                }
            }
        }
        {
            selector 'TableCell'
            values {
                verticalAlignment 'middle'
                padding '8'
            }
        }
        {
            selector 'Table.tableDark TableRow'
            values {
                decoration {
                    color '@c2'
                }
                textStyle {
                    color '@c1'
                }
            }
        }
        {
            selector 'Table.tableDark TableRow.body:hover'
            values {
                decoration {
                    color '@c6'
                }
                textStyle {
                    color '@c1'
                }
            }
        }
        {
            selector 'TableRow.darkRow'
            values {
                decoration {
                    color '@c7'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.lightRow'
            values {
                decoration {
                    color '@c1'
                }
                textStyle {
                    color '@c2'
                }
            }
        }
        {
            selector 'Table.tableHover TableRow.body:hover'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Table.tableSmall TableCell'
            values {
                padding '4'
            }
        }
        {
            selector 'Table.bordered'
            values {
                defaultColumnWidth '1.flex'
                defaultVerticalAlignment 'top'
                border {
                    top {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    left {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    right {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    bottom {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    horizontalInside {
                        color '@c7'
                        width '1'
                        style 'solid'
                    }
                    verticalInside {
                        color '@c7'
                        width '1'
                        style 'solid'
                    }
                }
            }
        }
        {
            selector 'Table.roundedborders'
            values {
                defaultColumnWidth '1.flex'
                defaultVerticalAlignment 'top'
                border {
                    top {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    left {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    right {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    bottom {
                        color '@c7'
                        width '1.0'
                        style 'solid'
                    }
                    horizontalInside {
                        color '@c7'
                        width '1'
                        style 'solid'
                    }
                    verticalInside {
                        color '@c7'
                        width '1'
                        style 'solid'
                    }
                    borderRadius '6'
                }
            }
        }
        {
            selector 'TableRow.bold'
            values {
                textStyle {
                    fontWeight 'bold'
                }
            }
        }
        {
            selector 'TableCell.bold'
            values {
                textStyle {
                    fontWeight 'bold'
                }
            }
        }
        {
            selector 'Table.headerborder TableRow.header'
            values {
                decoration {
                    border {
                        top {
                            color '@c15'
                            width '2'
                            style 'solid'
                        }
                        bottom {
                            color '@c15'
                            width '2'
                            style 'solid'
                        }
                    }
                }
            }
        }
        {
            selector 'Table.headercaption TableRow.header'
            values {
                decoration {
                    color '@c1'
                }
                textStyle {
                    color '@c2'
                    fontSize '16'
                    fontWeight 'bold'
                }
            }
        }
        {
            selector 'TableRow.tableActive'
            values {
                decoration {
                    color '@c4'
                }
            }
        }
        {
            selector 'TableRow.tableDefault'
            values {
                decoration {
                    color '@c1'
                }
            }
        }
        {
            selector 'TableRow.tablePrimary'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableSecondary'
            values {
                decoration {
                    color '@c3'
                }
            }
        }
        {
            selector 'TableRow.tableSuccess'
            values {
                decoration {
                    color '@c19'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableDanger'
            values {
                decoration {
                    color '@c31'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableWarning'
            values {
                decoration {
                    color '@c27'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableInfo'
            values {
                decoration {
                    color '@c23'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableDark'
            values {
                decoration {
                    color '@c7'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'TableRow.tableLight'
            values {
                decoration {
                    color '@c3'
                }
                textStyle {
                    color '@c2'
                }
            }
        }
        {
            selector 'Table.tableStriped TableRow:even'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'Table.tableStriped TableRow:odd'
            values {
                decoration {
                    color '@c19'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
         {
            selector 'InputField'
            values {
                activeColor '@c15'
                inActiveColor '@c4'
                padding '6 12'
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
                textStyle {
                    color '@c2'
                }
            }
        }
        {
            selector 'InputField:active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@15'
                        width '1'
                    }
                }
                textStyle {
                    color '@c2'
                }
            }
        }
        {
            selector 'InputField.small'
            values {
                height '30'
                padding '5 10'
                textStyle {
                    fontSize '12'
                }
            }
        }
        {
            selector 'InputField.large'
            values {
                height '46'
                padding '10 16'
                textStyle {
                    fontSize '16'
                }
            }
        }
        {
            selector 'DurationField InputField'
            values {
                padding '6 5'
                textAlign 'center'
                height '34'
                cornerRadius '4'
                activeColor '@c15'
                inActiveColor '@c4'
            }
        }
        {
            selector 'DurationField.disable InputField'
            values {
                decoration {
                    color '@c5'
                    border {
                        color '@c5'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'PasswordField Button'
            values {
                decoration {
                    color '@c5'
                }
                padding '5'
            }
        }
        {
            selector 'SearchableDropdown Container:hover,SearchableDropdown Container:selected'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'SearchableDropdown.searchablePopup'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'SearchResultView Container:hover'
            values {
                decoration {
                    color '@c15'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'SearchResultView.resultPopup'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'SearchComponent IconView'
            values {
                color '@c7'
                size '24'
            }
        }
        {
            selector 'SearchComponent InputField'
            values {
                activeColor '@c1'
                inActiveColor '@c1'
            }
        }
        {
            selector 'SearchComponent IconView:hover'
            values {
                color '@c15'
            }
        }
        {
            selector 'SearchComponent Row'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'SearchComponent Row:active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'VoiceBasedSearch Row'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'VoiceBasedSearch Row:active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'VoiceBasedSearch InputField'
            values {
                activeColor '@c1'
                inActiveColor '@c1'
            }
        }
        {
            selector 'DropDown'
            values {
                width '200'
                padding '10'
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'DropDownPopup'
            values {
                width '200'
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                    borderRadius '4'
                }
            }
        }
        {
            selector 'DurationField'
            values {
                margin '4 4 0 4'
            }
        }
        {
            selector 'SearchFilter'
            values {
                decoration {
                    border {
                        color '@c4'
                        width '1.0'
                    }
                    color '@c1'
                }
            }
        }
        {
            selector 'PasswordField'
            values {
                margin '4 4 0 4'
            }
        }
        {
            selector 'PasswordField Row'
            values {
                decoration {
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'PasswordField Row:active'
            values {
                decoration {
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'FloatingLabelField.bg TextView'
            values {
                backgroundColor '@c1'
            }
        }
         {
            selector 'CalenderView'
            values {
                decoration {
                    color '@c1'
                    borderRadius '8'
                }
                textStyle {
                    fontWeight 'bold'
                }
            }
        }
        {
            selector 'CalenderView.datePopup'
            values {
                width '400'
                decoration {
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'TimePickerWithInputfield.timePickerPopup'
            values {
                padding '10'
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'TimePicker.timePickerPopup'
            values {
                padding '10'
                decoration {
                    color '@c1'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'MonthOrYearCell'
            values {
                textStyle {
                    fontWeight 'bold'
                }
            }
        }
        {
            selector 'MonthOrYearCell:hover'
            values {
                textStyle {
                    color '@c15'
                }
            }
        }
        {
            selector 'DateCell'
            values {
                textStyle {
                    fontSize '15'
                    fontWeight 'bold'
                    color '@c2'
                }
            }
        }
        {
            selector 'DateCell:hover'
            values {
                decoration {
                    color '@c15'
                    borderRadius '5'
                }
                textStyle {
                    color '@c9'
                }
            }
        }
        {
            selector 'DateField'
            values {
                height '34'
                padding '0 12'
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateField.active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateField.disable'
            values {
                decoration {
                    color '@c5'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateField InputField'
            values {
                activeColor '00000000'
                inActiveColor '00000000'
            }
        }
        {
            selector 'TimeField InputField'
            values {
                activeColor '00000000'
                inActiveColor '00000000'
            }
        }
        {
            selector 'TimeField Row'
            values {
                height '34'
                padding '0 12'
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'TimeField Row.active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'TimeField.disable'
            values {
                decoration {
                    color '@c5'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateTimeField'
            values {
                padding '0 14'
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c4'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateTimeField.active'
            values {
                decoration {
                    color '@c1'
                    borderRadius '4'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'DateAndTimeCalendar'
            values {
                decoration {
                    border {
                        color '@c3'
                        width '1'
                    }
                    borderRadius '3'
                }
            }
        }
         {
            selector 'CalenderView IconButton:hover'
            values {
                decoration {
                    color '@c15'
                    borderRadius '5'
                }
            }
        }
         {
            selector 'DateTimeField IconView'
            values {
                color '@c2'
                size '24'
            }
        }
        {
            selector 'DateTimeField IconView:hover'
            values {
                color '@c15'
                size '24'
            }
        }
        {
            selector 'DateField IconView'
            values {
                color '@c2'
                size '24'
            }
        }
        {
            selector 'DateField IconView:hover'
            values {
                color '@c15'
                size '24'
            }
        }
         {
            selector 'CalenderView IconView'
            values {
                color '@c2'
                size '32'
            }
        }
        {
            selector 'TimeField IconView'
            values {
                color '@c2'
                size '24'
            }
        }
        {
            selector 'TimeField IconView:hover'
            values {
                color '@c15'
                size '24'
            }
        }
           {
            selector 'Radio.small IconView'
            values {
                color '@c2'
                size '16'
            }
        }
        {
            selector 'Radio.large IconView'
            values {
                color '@c2'
                size '24'
            }
        }
        {
            selector 'Radio IconView'
            values {
                color '@c2'
                size '20'
            }
        }
        {
            selector 'Radio:active IconView'
            values {
                color '@c15'
            }
        }
        {
            selector 'ProfileWithEditIcon IconView'
            values {
                color '@c2'
                size '16'
            }
        }
        {
            selector 'ProfileWithStatus IconView'
            values {
                color '@c15'
                size '16'
            }
        }
        {
            selector 'Radio:disabled'
            values {
                decoration {
                    color '@c4'
                    borderRadius '15'
                }
            }
        }
        {
            selector 'QuestionWithRadio Column'
            values {
                padding '5 10'
                decoration {
                    color '@c3'
                }
            }
        }
        {
            selector 'SatisfactionSurveyGrid'
            values {
                decoration {
                    color '@c3'
                }
                padding '10'
            }
        }
        {
            selector 'SatisfactionSurveyGrid TextView'
            values {
                color '@c2'
                textAlign 'center'
                softWrap 'true'
                margin '10 0'
            }
        }

         {
            selector '.bgprimary'
            values {
                decoration {
                    color '@c17'
                }
            }
        }
        {
            selector '.bgsuccess'
            values {
                decoration {
                    color '@c21'
                }
            }
        }
        {
            selector '.bginfo'
            values {
                decoration {
                    color '@c25'
                }
            }
        }
        {
            selector '.bgwarning'
            values {
                decoration {
                    color '@c29'
                }
            }
        }
        {
            selector '.bgdanger'
            values {
                decoration {
                    color '@c33'
                }
            }
        }
        {
            selector '.borderColor'
            values {
                decoration {
                    border {
                        color '@c3'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'MouseHoverView'
            values {
                decoration {
                    color '@c5'
                }
            }
        }
        {
            selector 'MouseHoverView.mousePointer'
            values {
                decoration {
                    color '@c5'
                }
            }
        }
        {
            selector 'ProgressBar Row'
            values {
                height '10'
                decoration {
                    color '@c3'
                    border {
                        color '@c3'
                        width '1'
                    }
                    borderRadius '2'
                }
                width '100'
            }
        }
        {
            selector 'PopupWrapperView'
            values {
                decoration {
                    border {
                        color '@c5'
                        width '1'
                    }
                }
                padding '10'
            }
        }
        {
            selector 'ListView.SearchableDropdown'
            values {
                decoration {
                    border {
                        right {
                            color '@c4'
                            width '1.0'
                        }
                        left {
                            color '@c4'
                            width '1.0'
                        }
                        bottom {
                            color '@c4'
                            width '1.0'
                        }
                    }
                    color '@c1'
                }
            }
        }
        {
            selector 'ListView.SearchResultView'
            values {
                decoration {
                    border {
                        right {
                            color '@c4'
                            width '1.0'
                        }
                        left {
                            color '@c4'
                            width '1.0'
                        }
                        bottom {
                            color '@c4'
                            width '1.0'
                        }
                    }
                    color '@c1'
                }
            }
        }
        {
            selector 'PopupHeader'
            values {
                padding '10 20'
                decoration {
                    color '@c15'
                }
            }
        }
        {
            selector 'Chip Row'
            values {
                decoration {
                    color '@c1'
                    border {
                        color '@c7'
                        width '0.0'
                    }
                    borderRadius '16'
                }
            }
        }
        {
            selector 'AttachmentDownloadView'
            values {
                decoration {
                    color '@c14'
                    borderRadius '5'
                    border {
                        color '@c20'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'Badge'
            values {
                padding '10'
                decoration {
                    color '@c15'
                }
            }
        }
        {
            selector 'ProfileWithStatus'
            values {
                width '50'
                height '50'
                decoration {
                    color '@c1'
                    borderRadius '25'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'ProfileWithEditIcon'
            values {
                width '50'
                height '50'
                decoration {
                    color '@c1'
                    borderRadius '25'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'ProfileWithSubTextView Column.profile'
            values {
                width '50'
                height '50'
                decoration {
                    borderRadius '25'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'ProfileWithStatus Container.indicator'
            values {
                width '10'
                height '10'
                decoration {
                    color '@c15'
                    borderRadius '5'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'ProfileDividerView Container.profile'
            values {
                width '50'
                height '50'
                decoration {
                    color '@c15'
                    borderRadius '25'
                    border {
                        color '@c7'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'CarouselDot'
            values {
                width '10'
                height '10'
                margin '5'
                decoration {
                    color '@c15'
                    shape 'circle'
                }
            }
        }
        {
            selector 'CarouselView ImageView'
            values {
                width '250'
                height '250'
            }
        }
         {
            selector 'CarouselView TextView'
            values {
                fontSize '16'
                color '00ff0000'
            }
        }
        {
            selector 'PopupHeader TextView'
            values {
                color '@c1'
                fontSize '18'
                fontWeight 'w700'
            }
        }
        {
            selector 'Badge TextView'
            values {
                color '@c9'
                fontSize '18'
                fontWeight 'w700'
                textAlign 'center'
            }
        }
        {
            selector 'Divider Container'
            values {
                decoration {
                    color '@c3'
                }
            }
        }
        {
            selector 'ProgressBar Container'
            values {
                height '5'
                decoration {
                    color '@c15'
                    borderRadius '2'
                    border {
                        color '@c15'
                        width '1'
                    }
                }
            }
        }
        {
            selector 'HelpView Container'
            values {
                alignment 'center'
                decoration {
                    color '@c3'
                }
                width '35'
                height '35'
            }
        }
        {
            selector 'CarouselView Container'
            values {
                decoration {
                    color '@c3'
                    borderRadius '10'
                }
            }
        }
        {
            selector 'Slider Container.maxValueBox'
            values {
                decoration {
                    color '@c5'
                    borderRadius '4'
                }
                padding '5'
                height '40'
                width '40'
                margin '0 10 0 0'
                alignment 'center'
            }
        }
        {
            selector 'Slider Container.roundSlider'
            values {
                width '20'
                height '20'
                decoration {
                    color '@c15'
                    shape 'circle'
                }
            }
        }
        {
            selector 'Slider Container.minValueBox'
            values {
                decoration {
                    color '@c5'
                    borderRadius '4'
                }
                padding '5'
                height '40'
                width '40'
                margin '0 0 0 10'
                alignment 'center'
            }
        }
        {
            selector 'QuantityCounter InputField'
            values {
                margin '0 10'
            }
        }
    ]
}