import React, { Component } from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import Checkbox from 'material-ui/Checkbox';
import FlatButton from 'material-ui/FlatButton';

class Led extends Component {
    constructor(props) {
        super(props);

        this.state = {
            on: !!this.props.led.state,
        }
    }

    toggleLight() {
        this.setState((oldState) => {
            return {
                on: !oldState.on,
            };
        });
    }

    render() {
        return (
            <Card>
                <CardTitle title={`LED #${this.props.led.id}`} subtitle="Card subtitle"/>
                <CardActions>
                    <Checkbox
                        checked={this.state.on}
                        onCheck={this.toggleLight.bind(this)}
                        label="Custom icon of different shapes"
                    />
                </CardActions>
            </Card>
        );
    }
}

export default Led;