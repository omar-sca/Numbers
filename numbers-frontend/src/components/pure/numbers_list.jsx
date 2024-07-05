import React, { } from "react";
import PropTypes from "prop-types";
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/style.css';

const NumbersList = ({ n_list }) => {

    return (
        <ul className="list-group list-group-horizontal my-2 d-flex flex-wrap">
            { n_list.length > 0 ? 
                n_list.map((number, index) =>
                    <li className="list-group-item my-1" key={index} > { number }</li>) 
                :
                <li className="list-group-item my-1">Error!</li>
            }
        </ul>
	);
}


NumbersList.propTypes = {
	// n_list: PropTypes.instanceOf(Array[Number])
};

export default NumbersList;
