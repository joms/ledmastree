import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux'
import { fetchLeds, setLedState } from "../redux/actions";
import LedList from '../components/LedList';


class LedContainer extends Component {
    constructor(props) {
        super(props);
        this.onChange = this.onChange.bind(this);
    }

    componentDidMount() {
        this.props.dispatch(fetchLeds());
    }

    onChange(id, state) {
        this.props.dispatch(setLedState(id, state));
    }

    render() {
        const { leds } = this.props;

        return (
            <LedList leds={leds} onChange={this.onChange}/>
        );
    }
}

function mapStateToProps(state) {
    const { leds } = state;

    return {
        leds,
    }
}

export default connect(mapStateToProps)(LedContainer);