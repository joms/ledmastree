import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, { Component } from 'react';
import LedContainer from './containers/LedContainer';

class App extends Component {
    render() {
        return (
            <MuiThemeProvider>
                <LedContainer/>
            </MuiThemeProvider>
        );
    }
}

export default App;