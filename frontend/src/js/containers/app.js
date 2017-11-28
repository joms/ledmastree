import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import {fetchLeds} from "../redux/actions/index";


class App extends Component {
    componentDidMount() {
        const { dispatch } = this.props;
        dispatch(fetchLeds());
    }

    render() {
        const { leds } = this.props;
        console.log(leds);

        return (
            <MuiThemeProvider>
                <h1>Hello, world</h1>
            </MuiThemeProvider>
        );
    }
}

function mapStateToProps(state) {
    const leds = state.leds;

    console.log(state);

    return {
        leds
    };
}

export default connect(mapStateToProps)(App);