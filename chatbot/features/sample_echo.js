/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License.
 */

module.exports = function(controller) {

    controller.hears('Bonjour','message,direct_message', async(bot, message) => {
        await bot.beginDialog('bonsoir');
    });

    controller.hears('Qui vit dans un ananas au fond de la mer','message,direct_message', async(bot, message) => {
        await bot.reply(message, 'Bob l\'éponge carrée');
    });

    controller.hears('Bonsoir','message,direct_message', async(bot, message) => {
        await bot.reply(message, 'Bonjour');
    });

    controller.on('message,direct_message', async(bot, message) => {
        await bot.reply(message, `G pa compri`);
    });
}

