class CostEstimator:

    hours: int
    estimated_salary: float
    only_weekends: bool
    months: float
    total_hours: float
    days_per_week: int = 2
    MINIMUM_PROJECT_DELAY_PERCENTAGE: float = 0.15
    FIXED_MEAN_COST: float = 350
    cost_per_hour: float
    final_cost: float

    def set_hours(self, hours: int):
        self.hours = hours

    def set_estimated_salary(self, estimated_salary: float):
        self.estimated_salary = estimated_salary

    def set_only_weekends(self, only_weekends: str):
        if only_weekends != 's' and only_weekends != 'n':
            self.set_only_weekends(only_weekends)
            return

        self.only_weekends = True if only_weekends == 's' else False

    def set_days_per_week(self, weekends_too: str):
        if not self.only_weekends:
            self.days_per_week = 5
            if weekends_too != 's' and weekends_too != 'n':
                self.set_days_per_week(weekends_too)
                return

            if weekends_too == 's':
                self.days_per_week += 2

    def set_months(self, months: float):
        self.months = months

    def calculate_final_costs(self):
        total_days: float
        weeks_in_month = 4
        if self.days_per_week == 2:
            total_days = (self.months * weeks_in_month)
        else:
            total_days = (self.months * (self.days_per_week * weeks_in_month))

        self.total_hours = total_days * self.hours
        self.total_hours += self.total_hours * self.MINIMUM_PROJECT_DELAY_PERCENTAGE

        self.cost_per_hour = (self.estimated_salary + self.FIXED_MEAN_COST) // self.total_hours
        self.final_cost = self.cost_per_hour * (self.total_hours * self.months)

    def show_final_costs(self):
        print('Custo do projeto por hora: {:.2f}'.format(self.cost_per_hour))
        print('Custo total do projeto: {:.2f}'.format(self.final_cost))


if __name__ == '__main__':
    cost_estimator = CostEstimator()

    cost_estimator.set_hours(int(input('Coloque o número de horas que vai trabalhar por dia: ')))
    cost_estimator.set_estimated_salary(float(input('Insira seu salário atual ou estimado: ')))
    cost_estimator.set_only_weekends(input('Vai trabalhar apenas nos finais de semana? (s/n) ').lower())
    cost_estimator.set_months(float(input('Insira a estimativa de meses para terminar o projeto (sem "gordura"): ')))
    if cost_estimator.days_per_week > 2:
        cost_estimator.set_days_per_week(input('Vai trabalhar tambem nos finais de semana? '))

    cost_estimator.calculate_final_costs()
    cost_estimator.show_final_costs()
