import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, { Component } from 'react';
import { connect } from 'react-redux';

import MyAwesomeReactComponent from '../components/awesome';

class App extends Component {
    render() {
        return (
            <MuiThemeProvider>
                <MyAwesomeReactComponent/>
            </MuiThemeProvider>
        );
    }
}

export default App;