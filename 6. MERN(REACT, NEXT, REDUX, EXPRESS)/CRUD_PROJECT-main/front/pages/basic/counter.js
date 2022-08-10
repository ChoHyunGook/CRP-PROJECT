import React from 'react';
import { connect } from 'react-redux';
import { increase, decrease } from '@/modules/basic/counter';
import { Counter } from '@/components/basic/Counter';

const CounterPage = ({ number, increase, decrease }) => {
  return (
    <Counter
      number={number}
      onIncrease={increase}
      onDecrease={decrease}
    />
  );
};

const mapStateToProps = state => ({number: state.counter})

const registerActions = {
  increase,
  decrease
}

export default connect(mapStateToProps, registerActions)(CounterPage);