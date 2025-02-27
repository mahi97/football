# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.






from . import *


def build_scenario(builder):
  builder.SetFlag('game_duration', 400)
  builder.SetFlag('deterministic', False)
  builder.SetFlag('offsides', False)
  builder.SetFlag('end_episode_on_score', True)
  builder.SetFlag('end_episode_on_out_of_play', True)
  builder.SetFlag('end_episode_on_possession_change', False)

  builder.SetBallPosition(0.99, 0.41)

  builder.SetTeam(Team.e_Home)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(1.0, 0.42, e_PlayerRole_LB)
  builder.AddPlayer(0.7, 0.15, e_PlayerRole_CB)
  builder.AddPlayer(0.7, 0.05, e_PlayerRole_CB)
  builder.AddPlayer(0.7, -0.05, e_PlayerRole_RB)
  builder.AddPlayer(0.0, 0.0, e_PlayerRole_CM)
  builder.AddPlayer(0.6, 0.35, e_PlayerRole_CM)
  builder.AddPlayer(0.8, 0.07, e_PlayerRole_CM)
  builder.AddPlayer(0.8, -0.03, e_PlayerRole_LM)
  builder.AddPlayer(0.8, -0.13, e_PlayerRole_RM)
  builder.AddPlayer(0.7, -0.3, e_PlayerRole_CF)

  builder.SetTeam(Team.e_Away)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(-0.75, -0.18, e_PlayerRole_LB)
  builder.AddPlayer(-0.75, -0.08, e_PlayerRole_CB)
  builder.AddPlayer(-0.75, 0.02, e_PlayerRole_CB)
  builder.AddPlayer(-1.0, -0.1, e_PlayerRole_RB)
  builder.AddPlayer(-0.8, -0.25, e_PlayerRole_CM)
  builder.AddPlayer(-0.88, -0.07, e_PlayerRole_CM)
  builder.AddPlayer(-0.88, 0.03, e_PlayerRole_CM)
  builder.AddPlayer(-0.88, 0.13, e_PlayerRole_LM)
  builder.AddPlayer(-0.75, 0.25, e_PlayerRole_RM)
  builder.AddPlayer(-0.2, 0.0, e_PlayerRole_CF)
