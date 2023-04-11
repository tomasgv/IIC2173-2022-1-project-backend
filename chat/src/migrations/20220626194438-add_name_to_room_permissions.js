'use strict';

module.exports = {
  /**
   * @typedef {import('sequelize').Sequelize} Sequelize
   * @typedef {import('sequelize').QueryInterface} QueryInterface
   */

  /**
   * @param {QueryInterface} queryInterface
   * @param {Sequelize} Sequelize
   * @returns
   */
   up: async (queryInterface, Sequelize) => {
    queryInterface.addColumn(
      'Room_permissions',
      'name',
      {
        type: Sequelize.STRING,
        defaultValue: false,
        allowNull: false,
      },
    );
  },

  down: async (queryInterface, Sequelize) => {
    queryInterface.removeColumn(
      'Room_permissions',
      'name',
    );
  },
};
