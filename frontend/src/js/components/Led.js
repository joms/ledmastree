import React, { Component } from 'react'
import PropTypes from 'prop-types';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import Toggle from 'material-ui/Toggle';


export default class Led extends Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(e, state) {
        const { onLedChange } = this.props;
        onLedChange(this.props.id, state);
    }

    render() {
        const { id, state } = this.props;

        return (
            <Card>
                <CardTitle title={`LED #${id}`}/>
                <CardActions>
                    <Toggle
                        toggled={state}
                        onToggle={this.onChange}
                        style={{marginBottom: 16}}
                    />
                </CardActions>
            </Card>
        )
    }
};