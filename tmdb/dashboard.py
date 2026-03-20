from visualizations import plot_revenue_vs_budget, plot_roi_by_genre, plot_popularity_vs_rating, plot_yearly_box_office, plot_franchise_vs_standalone


def dashboard():
    plot_revenue_vs_budget()
    plot_roi_by_genre()
    plot_popularity_vs_rating()
    plot_yearly_box_office()
    plot_franchise_vs_standalone()


if __name__ == "__main__":
    print(dashboard())
