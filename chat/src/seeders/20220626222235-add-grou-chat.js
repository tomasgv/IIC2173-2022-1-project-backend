'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    await queryInterface.bulkInsert(
      'Rooms',
      [
        {
          uuid: 'c50d542f-bc78-45ba-9ccb-fd4d1c4ddc60',
          name: 'Chat masivo',
          entity_owner: '52215ef7-8968-48fe-b138-fe40ed132c87',
          level_admin: 99,
          type: 'group',
          max_entity_rules: 1000,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete('Rooms', {
      [Op.or]: [{ name: 'Chat masivo' }],
    });
  },
};
