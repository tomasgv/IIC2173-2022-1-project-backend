Rails.application.routes.draw do
  # devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  #

  resources :users, only: [:create, :index, :show, :update] do
    resources :locations, only: [:create, :index, :update]
  end

  resources :tags, only: [:index]

  resources :pings, only: [:create, :index, :update]

  get "/user_tags/:id", to: "users#user_tags"
  get "/location_tags/:id", to: "locations#location_tags"

  get "/sent_pings", to: "pings#sent_pings"
end
