import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import LedContainer from './ledContainer';

import { fetchLeds } from "../redux/actions/index";


class App extends Component {
    componentDidMount() {
        const { dispatch } = this.props;
        dispatch(fetchLeds());
    }

    render() {
        const { leds } = this.props;

        return (
            <MuiThemeProvider>
                <LedContainer leds={leds} />
            </MuiThemeProvider>
        );
    }
}

function mapStateToProps(state) {
    const leds = state.leds;

    return {
        leds
    };
}

export default connect(mapStateToProps)(App);