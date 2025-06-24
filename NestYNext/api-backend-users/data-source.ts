import { DataSource } from 'typeorm';

export const AppDataSource = new DataSource({
  type: 'mysql', // o 'postgres', 'sqlite', etc.
  host: 'localhost',
  port: 3306,
  username: 'root',
  password: '',
  database: 'nest_users_db',
  entities: ['src/**/*.entity.ts'], // Usa .ts si generas migraciones en desarrollo
  migrations: ['src/migrations/*.ts'], // Ruta donde se crearán tus migraciones
  synchronize: false,
});
