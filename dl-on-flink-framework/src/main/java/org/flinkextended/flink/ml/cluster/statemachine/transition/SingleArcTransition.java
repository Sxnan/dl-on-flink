/*
 * Copyright 2022 Deep Learning on Flink Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.flinkextended.flink.ml.cluster.statemachine.transition;

import org.flinkextended.flink.ml.cluster.statemachine.InvalidStateTransitionException;

/**
 * Hook for Transition. This lead to state machine to move to the post state as registered in the
 * state machine.
 */
public interface SingleArcTransition<OPERAND, EVENT> {
    /**
     * Transition hook.
     *
     * @param operand the entity attached to the FSM, whose internal state may change.
     * @param event causal event
     */
    void transition(OPERAND operand, EVENT event) throws InvalidStateTransitionException;
}
