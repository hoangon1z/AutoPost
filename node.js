import connection from "../config/connectDB";
import winGoController from "./winGoController";
import k5Controller from "./k5Controller";
import k3Controller from "./k3Controller";

import cron from 'node-cron';

const cronJobGame1p = (io) => {
    cron.schedule('*/1 * * * *', async() => {
        await winGoController.addWinGo(1);
        await winGoController.handlingWinGo1P(1);
        const [winGo1] = await connection.execute('SELECT * FROM `wingo` WHERE `game` = "wingo" ORDER BY `id` DESC LIMIT 2 ', []);
        const data = winGo1; // Cầu mới chưa có kết quả
        io.emit('data-server', { data: data });

        await k5Controller.add5D(1);
        await k5Controller.handling5D(1);
        const [k5D] = await connection.execute('SELECT * FROM 5d WHERE `game` = 1 ORDER BY `id` DESC LIMIT 2 ', []);
        const data2 = k5D; // Cầu mới chưa có kết quả
        io.emit('data-server-5d', { data: data2, 'game': '1' });

        await k3Controller.addK3(1);
        await k3Controller.handlingK3(1);
        const [k3] = await connection.execute('SELECT * FROM k3 WHERE `game` = 1 ORDER BY `id` DESC LIMIT 2 ', []);
        const data3 = k3; // Cầu mới chưa có kết quả
        io.emit('data-server-k3', { data: data3, 'game': '1' });
    });
    cron.schedule('*/3 * * * *', async() => {
        await winGoController.addWinGo(3);
        await winGoController.handlingWinGo1P(3);
        const [winGo1] = await connection.execute('SELECT * FROM `wingo` WHERE `game` = "wingo3" ORDER BY `id` DESC LIMIT 2 ', []);
        const data = winGo1; // Cầu mới chưa có kết quả
        io.emit('data-server', { data: data });

        await k5Controller.add5D(3);
        await k5Controller.handling5D(3);
        const [k5D] = await connection.execute('SELECT * FROM 5d WHERE `game` = 3 ORDER BY `id` DESC LIMIT 2 ', []);
        const data2 = k5D; // Cầu mới chưa có kết quả
        io.emit('data-server-5d', { data: data2, 'game': '3' });

        await k3Controller.addK3(3);
        await k3Controller.handlingK3(3);
        const [k3] = await connection.execute('SELECT * FROM k3 WHERE `game` = 3 ORDER BY `id` DESC LIMIT 2 ', []);
        const data3 = k3; // Cầu mới chưa có kết quả
        io.emit('data-server-k3', { data: data3, 'game': '3' });
    });
    cron.schedule('*/5 * * * *', async() => {
        await winGoController.addWinGo(5);
        await winGoController.handlingWinGo1P(5);
        const [winGo1] = await connection.execute('SELECT * FROM `wingo` WHERE `game` = "wingo5" ORDER BY `id` DESC LIMIT 2 ', []);
        const data = winGo1; // Cầu mới chưa có kết quả
        io.emit('data-server', { data: data });

        await k5Controller.add5D(5);
        await k5Controller.handling5D(5);
        const [k5D] = await connection.execute('SELECT * FROM 5d WHERE `game` = 5 ORDER BY `id` DESC LIMIT 2 ', []);
        const data2 = k5D; // Cầu mới chưa có kết quả
        io.emit('data-server-5d', { data: data2, 'game': '5' });

        await k3Controller.addK3(5);
        await k3Controller.handlingK3(5);
        const [k3] = await connection.execute('SELECT * FROM k3 WHERE `game` = 5 ORDER BY `id` DESC LIMIT 2 ', []);
        const data3 = k3; // Cầu mới chưa có kết quả
        io.emit('data-server-k3', { data: data3, 'game': '5' });
    });
    cron.schedule('*/10 * * * *', async() => {
        await winGoController.addWinGo(10);
        await winGoController.handlingWinGo1P(10);
        const [winGo1] = await connection.execute('SELECT * FROM `wingo` WHERE `game` = "wingo10" ORDER BY `id` DESC LIMIT 2 ', []);
        const data = winGo1; // Cầu mới chưa có kết quả
        io.emit('data-server', { data: data });

        
        await k5Controller.add5D(10);
        await k5Controller.handling5D(10);
        const [k5D] = await connection.execute('SELECT * FROM 5d WHERE `game` = 10 ORDER BY `id` DESC LIMIT 2 ', []);
        const data2 = k5D; // Cầu mới chưa có kết quả
        io.emit('data-server-5d', { data: data2, 'game': '10' });

        await k3Controller.addK3(10);
        await k3Controller.handlingK3(10);
        const [k3] = await connection.execute('SELECT * FROM k3 WHERE `game` = 10 ORDER BY `id` DESC LIMIT 2 ', []);
        const data3 = k3; // Cầu mới chưa có kết quả
        io.emit('data-server-k3', { data: data3, 'game': '10' });
    });

    cron.schedule('* * 0 * * *', async() => {
        await connection.execute('UPDATE users SET roses_today = ?', [0]);
        await connection.execute('UPDATE point_list SET money = ?', [0]);
        await connection.execute('UPDATE users SET roses_f1 = ?', [0]);
        await connection.execute('UPDATE users SET roses_f = ?', [0]);
        await connection.execute('UPDATE users SET total_roses = ?', [0]);
    });

}

module.exports = {
    cronJobGame1p
};
const addWinGo = async (game) => {
    try {
        let join = '';
        if (game == 1) join = 'wingo';
        if (game == 3) join = 'wingo3';
        if (game == 5) join = 'wingo5';
        if (game == 10) join = 'wingo10';

        const [winGoNow] = await connection.query(`SELECT period FROM wingo WHERE status = 0 AND game = "${join}" ORDER BY id DESC LIMIT 1 `);
        const [setting] = await connection.query('SELECT * FROM `admin` ');
        let period = winGoNow[0].period; // cầu hiện tại
        let amount = Math.floor(Math.random() * 10); // xanh đỏ tím
        let timeNow = Date.now();

        let nextResult = '';
        if (game == 1) nextResult = setting[0].wingo1;
        if (game == 3) nextResult = setting[0].wingo3;
        if (game == 5) nextResult = setting[0].wingo5;
        if (game == 10) nextResult = setting[0].wingo10;

        let newArr = '';
        if (nextResult == '-1') {
            await connection.execute(`UPDATE wingo SET amount = ?,status = ? WHERE period = ? AND game = "${join}"`, [amount, 1, period]);
            newArr = '-1';
        } else {
            let result = '';
            let arr = nextResult.split('|');
            let check = arr.length;
            if (check == 1) {
                newArr = '-1';
            } else {
                for (let i = 1; i < arr.length; i++) {
                    newArr += arr[i] + '|';
                }
                newArr = newArr.slice(0, -1);
            }
            result = arr[0];
            await connection.execute(`UPDATE wingo SET amount = ?,status = ? WHERE period = ? AND game = "${join}"`, [result, 1, period]);
        }
        const sql3 = 'INSERT INTO `wingo` SET `period` = ?, `amount` = ?, `game` = ?, `status` = ?, `time` = ?';
        await connection.execute(sql3, [Number(period) + 1, 0, join, 0, timeNow]);

        if (game == 1) join = 'wingo1';
        if (game == 3) join = 'wingo3';
        if (game == 5) join = 'wingo5';
        if (game == 10) join = 'wingo10';

        await connection.execute(`UPDATE admin SET ${join} = ?`, [newArr]);
    } catch (error) {
        if (error) {
            console.log(error);
        }
    }
}
