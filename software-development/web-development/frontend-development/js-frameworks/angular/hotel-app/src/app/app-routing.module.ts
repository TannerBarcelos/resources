import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ReservationFormComponent } from './reservation-form/reservation-form.component';
import { ReservationListComponent } from './reservation-list/reservation-list.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent, // Component (page) to render when hitting /
  },
  {
    path: 'new',
    component: ReservationFormComponent, // Component (page) to render when hitting /new
  },
  {
    path: 'list',
    component: ReservationListComponent, // Component (page) to render when hitting /list
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
